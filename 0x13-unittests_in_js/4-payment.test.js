const { spy, stub } = require('sinon');

const sendPaymentRequestToApi = require('./3-payment');
const utils = require('./utils');
const { expect } = require('chai');

describe('Test sendPaymentRequestToApi function', () => {
  it('Test the console output', () => {
    const moduleStub = stub(utils, 'calculateNumber');
    const consoleSpy = spy(console, 'log');

    moduleStub.returns(10);

    sendPaymentRequestToApi(100, 20);

    expect(moduleStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledWithExactly('The total is: 10')).to.be.true;

    moduleStub.restore();
    consoleSpy.restore();
  });
});
