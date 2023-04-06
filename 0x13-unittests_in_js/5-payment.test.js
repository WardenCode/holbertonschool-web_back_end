const sendPaymentRequestToApi = require('./5-payment');
const { spy } = require('sinon');
const { expect } = require('chai');

describe('Test sendPaymentRequestToAPI', () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = spy(console, 'log');
  });

  afterEach(() => {
    consoleSpy.restore();
  });

  it('Test sendPaymentRequestToAPI with 100, and 20', () => {
    sendPaymentRequestToApi(100, 20);
    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
  });

  it('Test sendPaymentRequestToAPI with 10, and 10', () => {
    sendPaymentRequestToApi(10, 10);
    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
  });
});
