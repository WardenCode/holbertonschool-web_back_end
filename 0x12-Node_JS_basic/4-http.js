const http = require('http');

const host = 'localhost';
const port = 1245;

const requestListener = (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.write('Hello Holberton School!');
  res.end();
};

const app = http.createServer(requestListener);

app.listen(port, host);

module.exports = app;
