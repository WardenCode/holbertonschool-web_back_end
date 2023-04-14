import redis from 'redis';

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

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, value) => {
        if (err) {
            console.error(err);
            return;
        }
        console.log(value);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');