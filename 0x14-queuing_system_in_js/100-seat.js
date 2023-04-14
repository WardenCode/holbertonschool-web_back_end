import redis from 'redis';
import kue from 'kue';
import express from 'express';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.set('availableSeats', 50);
let reservationEnabled = true;

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const getCurrentAvailableSeats = async () => parseInt(await getAsync('availableSeats'));

const reserveSeat = async (number, available_seats) => {
    if ((available_seats - number) < 0) return;

    await setAsync('availableSeats', available_seats - number);
};

const queue = kue.createQueue();

const app = express();

const port = 1245;
const hostname = 'localhost';

app.get('/available_seats', async (req, res) => {
    const seats = await getCurrentAvailableSeats();

    res.json({"numberOfAvailableSeats": seats});
});

app.get('/reserve_seat', async (req, res) => {
    if (!reservationEnabled) {
        return res.json({"status": "Reservation are blocked"})
    }

    const job = queue.create('reserve_seat', {});

    job.save((err) => {
        if (err) {
            return res.json({ "status": "Reservation failed" });
        }

        return res.json({ "status": "Reservation in process" });
    })

    job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`)
    });

    job.on('failed', (err) => {
        console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });
});

app.get('/process', (req, res) => {
    queue.process('reserve_seat', async (job, done) => {
        let availableSeats = await getCurrentAvailableSeats();

        if (availableSeats <= 0) {
            reservationEnabled = false;
            done(Error('Not enough seats available'));
        }

        await reserveSeat(1, availableSeats);

        availableSeats = await getCurrentAvailableSeats();

        done();
    });

    res.json({ "status": "Queue processing" });
});

app.listen(port, hostname, () => {
    console.log(`app listen in port: ${port}`)
});