const http = require('http');
const { argv } = require('process');
const countStudents = require('./3-read_file_async');

const host = 'localhost';
const port = 1245;

const requestListener = (req, res) => {
  const { url } = req;

  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (url === '/students') {
    res.write('This is the list of our students\n');

    countStudents(argv[2])
      .then((msg) => res.end(msg))
      .catch(({ message }) => res.end(message));
  }
};

const app = http.createServer(requestListener);

app.listen(port, host);

module.exports = app;
