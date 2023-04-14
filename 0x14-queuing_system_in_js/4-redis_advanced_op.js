import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

const schools = {
    "Portland": 50,
    "Seattle": 80,
    "New York": 20,
    "Bogota": 20,
    "Cali": 40,
    "Paris": 2,
};

for (const [name, value] of Object.entries(schools)) {
    client.hset("HolbertonSchools", name, schools[name], (err, cb) => {
        if (err) {
            console.error(err);
            return;
        }
        redis.print(`Reply: ${cb}`);
    });
}

client.hgetall("HolbertonSchools", (err, cb) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(cb);
});