import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, (err, cb) => {
        if (err) {
            console.error(err);
            return;
        }

        redis.print(`Reply: ${cb}`);
    });
}

const get = promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
    try {
        const response = await get(schoolName);
        console.log(response);
    } catch (err) {
        throw err;
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');