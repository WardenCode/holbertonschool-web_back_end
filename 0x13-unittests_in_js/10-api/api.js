const express = require('express');

const port = 7865;
const hostname = 'localhost';

const app = express();

app.use(express.json());

app.get('/', (req, res) => {
  res.status(200);
  res.send('Welcome to the payment system');
});

app.get('/cart/:id([0-9]+)', (req, res) => {
  const { id } = req.params;
  res.status(200);
  res.send(`Payment methods for cart ${id}`);
});

app.get('/available_payments', (req, res) => {
  const dataResponse = {
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  };

  res.status(200);
  res.send(dataResponse);
});

app.post('/login', (req, res) => {
  const { userName } = req.body;

  if (!userName) {
    res.status(404);
    res.send('Please enter a valid userName');
    return;
  }

  res.status(200);
  res.send(`Welcome ${userName}`);
});

app.listen(port, hostname, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;
