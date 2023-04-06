const sum = (a, b) => a + b;

const subtract = (a, b) => a - b;

const divide = (a, b) => {
  if (b === 0) return 'Error';
  return a / b;
};

const calculateNumber = (type, a, b) => {
  const roundedA = Math.round(a);
  const roundedB = Math.round(b);
  let response = 0;

  const operations = {
    SUM: sum(roundedA, roundedB),
    SUBTRACT: subtract(roundedA, roundedB),
    DIVIDE: divide(roundedA, roundedB),
  };

  response = operations[type];

  if (response === undefined) throw TypeError;

  return response;
};

const Utils = {
  calculateNumber,
};

module.exports = Utils;
