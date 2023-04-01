const http = require('http');
const countStudents = require('./3-read_file_async');

const host = 'localhost';
const port = 1245;

const requestListener = (req, res) => {
  const { url } = req;

  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (url === '/') {
    res.write('Hello Holberton School!');
  } else if (url === '/students') {
    res.write('This is the list of our students\n');

    countStudents('database.csv')
      .then((msg) => res.end(msg))
      .catch((err) => res.end(err.message));
  }

  res.end();
};

const app = http.createServer(requestListener);

app.listen(port, host);

module.exports = app;
