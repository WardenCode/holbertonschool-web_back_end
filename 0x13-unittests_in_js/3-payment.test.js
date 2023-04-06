const sinon = require('sinon');

const sendPaymentRequestToApi = require('./3-payment');
const utils = require('./utils');
const { expect } = require('chai');

describe('Test sendPaymentRequestToApi function', () => {
  it('Test the console output', () => {
    const moduleSpy = sinon.spy(utils, 'calculateNumber');
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(moduleSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledWithExactly('The total is: 120')).to.be.true;

    moduleSpy.restore();
    consoleSpy.restore();
  });
});
