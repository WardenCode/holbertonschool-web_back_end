import redis from 'redis';

const client = redis.createClient();
const subscriber = client.duplicate();

client.on('connect', () => {
    console.log("Redis client connected to the server");
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

const channel = "holberton school channel";

subscriber.subscribe(channel);

subscriber.on('message', (channel, message) =>  {
    console.log(message);

    if (message === "KILL_SERVER") {
        subscriber.unsubscribe(channel);
        subscriber.quit();
    }
});