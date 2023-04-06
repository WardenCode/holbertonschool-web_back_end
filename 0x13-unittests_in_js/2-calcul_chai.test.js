const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('Test all operations of the function calculateNumber', () => {
  describe('Test SUM operation', () => {
    it('SUM operation with natural numbers', () => {
      expect(calculateNumber('SUM', 1, 2)).to.equal(3);
    });

    it('SUM operation with zeros', () => {
      expect(calculateNumber('SUM', 0, 0)).to.equal(0);
    });

    it('SUM operation with one zero', () => {
      expect(calculateNumber('SUM', 0, 5)).to.equal(5);
    });

    it('SUM operation with one negative number', () => {
      expect(calculateNumber('SUM', -1, 2)).to.equal(1);
    });

    it('SUM operation with two negative numbers', () => {
      expect(calculateNumber('SUM', -1, -2)).to.equal(-3);
    });

    it('SUM operation with one decimal point rounded to down', () => {
      expect(calculateNumber('SUM', 5.2, 6)).to.equal(11);
    });

    it('SUM operation with one decimal point rounded to up', () => {
      expect(calculateNumber('SUM', 5.6, 6)).to.equal(12);
    });

    it('SUM operation with two decimal point', () => {
      expect(calculateNumber('SUM', 5.3, 5.3)).to.equal(10);
    });

    it('SUM operation with two decimal point one round to top and one to down', () => {
      expect(calculateNumber('SUM', 5.6, 4.2)).to.equal(10);
    });

    it('SUM operation with two decimal point both round to top', () => {
      expect(calculateNumber('SUM', 5.6, 7.6)).to.equal(14);
    });

    it('SUM operation with two decimal point both round to down', () => {
      expect(calculateNumber('SUM', 5.4, 2.1)).to.equal(7);
    });

    it('SUM operation with two decimal point .0', () => {
      expect(calculateNumber('SUM', 5.0, 15.0)).to.equal(20);
    });
  });

  describe('Test SUBTRACT operation', () => {
    it('SUBTRACT operation with natural numbers', () => {
      expect(calculateNumber('SUBTRACT', 1, 2)).to.equal(-1);
    });

    it('SUBTRACT operation with zeros', () => {
      expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
    });

    it('SUBTRACT operation with one zero', () => {
      expect(calculateNumber('SUBTRACT', 0, 5)).to.equal(-5);
    });

    it('SUBTRACT operation with one negative number', () => {
      expect(calculateNumber('SUBTRACT', -1, 2)).to.equal(-3);
    });

    it('SUBTRACT operation with two negative numbers', () => {
      expect(calculateNumber('SUBTRACT', -1, -2)).to.equal(1);
    });

    it('SUBTRACT operation with one decimal point rounded to down', () => {
      expect(calculateNumber('SUBTRACT', 5.2, 6)).to.equal(-1);
    });

    it('SUBTRACT operation with one decimal point rounded to up', () => {
      expect(calculateNumber('SUBTRACT', 5.6, 6)).to.equal(0);
    });

    it('SUBTRACT operation with two decimal point', () => {
      expect(calculateNumber('SUBTRACT', 5.3, 5.3)).to.equal(0);
    });

    it('SUBTRACT operation with two decimal point one round to top and one to down', () => {
      expect(calculateNumber('SUBTRACT', 5.6, 4.2)).to.equal(2);
    });

    it('SUBTRACT operation with two decimal point both round to top', () => {
      expect(calculateNumber('SUBTRACT', 5.6, 7.6)).to.equal(-2);
    });

    it('SUBTRACT operation with two decimal point both round to down', () => {
      expect(calculateNumber('SUBTRACT', 5.4, 2.1)).to.equal(3);
    });

    it('SUBTRACT operation with two decimal point .0', () => {
      expect(calculateNumber('SUBTRACT', 5.0, 15.0)).to.equal(-10);
    });
  });

  describe('Test DIVIDE operation', () => {
    it('DIVIDE operation with natural numbers', () => {
      expect(calculateNumber('DIVIDE', 1, 2)).to.equal(0.5);
    });

    it('DIVIDE operation with zeros', () => {
      expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
    });

    it('DIVIDE operation with one zero', () => {
      expect(calculateNumber('DIVIDE', 0, 5)).to.equal(0);
    });

    it('DIVIDE operation with one negative number', () => {
      expect(calculateNumber('DIVIDE', -1, 2)).to.equal(-0.5);
    });

    it('DIVIDE operation with two negative numbers', () => {
      expect(calculateNumber('DIVIDE', -1, -2)).to.equal(0.5);
    });

    it('DIVIDE operation with one decimal point rounded to down', () => {
      expect(calculateNumber('DIVIDE', 10.2, 5)).to.equal(2);
    });

    it('DIVIDE operation with one decimal point rounded to up', () => {
      expect(calculateNumber('DIVIDE', 19.6, 4)).to.equal(5);
    });

    it('DIVIDE operation with two decimal point', () => {
      expect(calculateNumber('DIVIDE', 5.3, 5.3)).to.equal(1);
    });

    it('DIVIDE operation with two decimal point one round to top and one to down', () => {
      expect(calculateNumber('DIVIDE', 63.8, 8.2)).to.equal(8);
    });

    it('DIVIDE operation with two decimal point both round to top', () => {
      expect(calculateNumber('DIVIDE', 99.7, 24.9)).to.equal(4);
    });

    it('DIVIDE operation with two decimal point both round to down', () => {
      expect(calculateNumber('DIVIDE', 100.2, 2.4)).to.equal(50);
    });

    it('DIVIDE operation with two decimal point .0', () => {
      expect(calculateNumber('DIVIDE', 15.0, 5.0)).to.equal(3);
    });
  });

  describe('Test does not allowed operation', () => {
    it('Unknown operator', () => {
      expect(() => calculateNumber('UNKNOWN', 5, 5)).to.throw();
    });
  });
});
