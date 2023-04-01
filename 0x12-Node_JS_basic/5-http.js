const http = require('http');
const { argv } = require('process');
const countStudents = require('./3-read_file_async');

const host = 'localhost';
const port = 1245;

const requestListener = async (req, res) => {
  const { url } = req;

  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (url === '/') {
    res.write('Hello Holberton School!');
  } else if (url === '/students') {
    res.write('This is the list of our students\n');

    await countStudents(argv[2])
      .then((msg) => res.end(msg))
      .catch(({ message }) => res.end(message));
  }

  res.end();
};

const app = http.createServer(requestListener);

app.listen(port, host);

module.exports = app;
