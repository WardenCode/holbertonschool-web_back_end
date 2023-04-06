const express = require('express');

const port = 7865;
const hostname = 'localhost';

const app = express();

app.get('/', (req, res) => {
  res.status(200);
  res.send('Welcome to the payment system');
});

app.get('/cart/:id([0-9]+)', (req, res) => {
  const { id } = req.params;
  res.status(200);
  res.send(`Payment methods for cart ${id}`);
});

app.listen(port, hostname, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;
