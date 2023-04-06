const { strictEqual, throws } = require('assert');
const calculateNumber = require('./1-calcul');

describe('Test all operations of the function calculateNumber', () => {
  describe('Test SUM operation', () => {
    it('SUM operation with natural numbers', () => {
      strictEqual(calculateNumber('SUM', 1, 2), 3);
    });

    it('SUM operation with zeros', () => {
      strictEqual(calculateNumber('SUM', 0, 0), 0);
    });

    it('SUM operation with one zero', () => {
      strictEqual(calculateNumber('SUM', 0, 5), 5);
    });

    it('SUM operation with one negative number', () => {
      strictEqual(calculateNumber('SUM', -1, 2), 1);
    });

    it('SUM operation with two negative numbers', () => {
      strictEqual(calculateNumber('SUM', -1, -2), -3);
    });

    it('SUM operation with one decimal point rounded to down', () => {
      strictEqual(calculateNumber('SUM', 5.2, 6), 11);
    });

    it('SUM operation with one decimal point rounded to up', () => {
      strictEqual(calculateNumber('SUM', 5.6, 6), 12);
    });

    it('SUM operation with two decimal point', () => {
      strictEqual(calculateNumber('SUM', 5.3, 5.3), 10);
    });

    it('SUM operation with two decimal point one round to top and one to down', () => {
      strictEqual(calculateNumber('SUM', 5.6, 4.2), 10);
    });

    it('SUM operation with two decimal point both round to top', () => {
      strictEqual(calculateNumber('SUM', 5.6, 7.6), 14);
    });

    it('SUM operation with two decimal point both round to down', () => {
      strictEqual(calculateNumber('SUM', 5.4, 2.1), 7);
    });

    it('SUM operation with two decimal point .0', () => {
      strictEqual(calculateNumber('SUM', 5.0, 15.0), 20);
    });
  });

  describe('Test SUBTRACT operation', () => {
    it('SUBTRACT operation with natural numbers', () => {
      strictEqual(calculateNumber('SUBTRACT', 1, 2), -1);
    });

    it('SUBTRACT operation with zeros', () => {
      strictEqual(calculateNumber('SUBTRACT', 0, 0), 0);
    });

    it('SUBTRACT operation with one zero', () => {
      strictEqual(calculateNumber('SUBTRACT', 0, 5), -5);
    });

    it('SUBTRACT operation with one negative number', () => {
      strictEqual(calculateNumber('SUBTRACT', -1, 2), -3);
    });

    it('SUBTRACT operation with two negative numbers', () => {
      strictEqual(calculateNumber('SUBTRACT', -1, -2), 1);
    });

    it('SUBTRACT operation with one decimal point rounded to down', () => {
      strictEqual(calculateNumber('SUBTRACT', 5.2, 6), -1);
    });

    it('SUBTRACT operation with one decimal point rounded to up', () => {
      strictEqual(calculateNumber('SUBTRACT', 5.6, 6), 0);
    });

    it('SUBTRACT operation with two decimal point', () => {
      strictEqual(calculateNumber('SUBTRACT', 5.3, 5.3), 0);
    });

    it('SUBTRACT operation with two decimal point one round to top and one to down', () => {
      strictEqual(calculateNumber('SUBTRACT', 5.6, 4.2), 2);
    });

    it('SUBTRACT operation with two decimal point both round to top', () => {
      strictEqual(calculateNumber('SUBTRACT', 5.6, 7.6), -2);
    });

    it('SUBTRACT operation with two decimal point both round to down', () => {
      strictEqual(calculateNumber('SUBTRACT', 5.4, 2.1), 3);
    });

    it('SUBTRACT operation with two decimal point .0', () => {
      strictEqual(calculateNumber('SUBTRACT', 5.0, 15.0), -10);
    });
  });

  describe('Test DIVIDE operation', () => {
    it('DIVIDE operation with natural numbers', () => {
      strictEqual(calculateNumber('DIVIDE', 1, 2), 0.5);
    });

    it('DIVIDE operation with zeros', () => {
      strictEqual(calculateNumber('DIVIDE', 0, 0), 'Error');
    });

    it('DIVIDE operation with one zero', () => {
      strictEqual(calculateNumber('DIVIDE', 0, 5), 0);
    });

    it('DIVIDE operation with one negative number', () => {
      strictEqual(calculateNumber('DIVIDE', -1, 2), -0.5);
    });

    it('DIVIDE operation with two negative numbers', () => {
      strictEqual(calculateNumber('DIVIDE', -1, -2), 0.5);
    });

    it('DIVIDE operation with one decimal point rounded to down', () => {
      strictEqual(calculateNumber('DIVIDE', 10.2, 5), 2);
    });

    it('DIVIDE operation with one decimal point rounded to up', () => {
      strictEqual(calculateNumber('DIVIDE', 19.6, 4), 5);
    });

    it('DIVIDE operation with two decimal point', () => {
      strictEqual(calculateNumber('DIVIDE', 5.3, 5.3), 1);
    });

    it('DIVIDE operation with two decimal point one round to top and one to down', () => {
      strictEqual(calculateNumber('DIVIDE', 63.8, 8.2), 8);
    });

    it('DIVIDE operation with two decimal point both round to top', () => {
      strictEqual(calculateNumber('DIVIDE', 99.7, 24.9), 4);
    });

    it('DIVIDE operation with two decimal point both round to down', () => {
      strictEqual(calculateNumber('DIVIDE', 100.2, 2.4), 50);
    });

    it('DIVIDE operation with two decimal point .0', () => {
      strictEqual(calculateNumber('DIVIDE', 15.0, 5.0), 3);
    });
  });

  describe('Test does not allowed operation', () => {
    it('Unknown operator', () => {
      throws(() => calculateNumber('UNKNOWN', 5, 5), '[Function: TypeError]');
    });
  });
});
