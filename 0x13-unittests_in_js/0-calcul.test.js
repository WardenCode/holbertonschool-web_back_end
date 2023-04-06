const calculateNumber = require('./0-calcul');
const assert = require('assert');

describe('calculateNumber test sum numbers and rounds it', () => {
  it('Test with natural numbers', () => {
    assert.strictEqual(calculateNumber(1, 2), 3);
  });

  it('Test with zeros', () => {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });

  it('Test one zero', () => {
    assert.strictEqual(calculateNumber(0, 5), 5);
  });

  it('Test with one negative number', () => {
    assert.strictEqual(calculateNumber(-1, 2), 1);
  });

  it('Test with two negative numbers', () => {
    assert.strictEqual(calculateNumber(-1, -2), -3);
  });

  it('Test with one decimal point rounded to down', () => {
    assert.strictEqual(calculateNumber(5.2, 6), 11);
  });

  it('Test with one decimal point rounded to up', () => {
    assert.strictEqual(calculateNumber(5.6, 6), 12);
  });

  it('Test with two decimal point', () => {
    assert.strictEqual(calculateNumber(5.3, 5.3), 10);
  });

  it('Test with two decimal point one round to top and one to down', () => {
    assert.strictEqual(calculateNumber(5.6, 4.2), 10);
  });

  it('Test with two decimal point both round to top', () => {
    assert.strictEqual(calculateNumber(5.6, 7.6), 14);
  });

  it('Test with two decimal point both round to down', () => {
    assert.strictEqual(calculateNumber(5.4, 2.1), 7);
  });

  it('Test with two decimal point .0', () => {
    assert.strictEqual(calculateNumber(5.0, 15.0), 20);
  });
});
