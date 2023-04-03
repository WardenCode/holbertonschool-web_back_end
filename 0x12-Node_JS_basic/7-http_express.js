const express = require('express');
const { argv } = require('process');

const countStudents = require('./3-read_file_async');

const app = express();

const port = 1245;

app.get('/', (req, res) => res.send('Hello Holberton School!'));

app.get('/students', async (req, res) => {
  const headerMsg = 'This is the list of our students\n';
  await countStudents(argv[2])
    .then((data) => res.send(`${headerMsg}${data}`))
    .catch((err) => res.send(`${headerMsg}${err.message}`));
});

app.listen(port);

module.exports = app;
