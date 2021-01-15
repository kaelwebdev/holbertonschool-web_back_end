const sinon = require('sinon');
const { expect } = require('chai')
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
    const spy = sinon.spy(Utils, 'calculateNumber');
  
    it('check arguments (SUM, 100, 20) and call', () => {
        sendPaymentRequestToApi(100, 20);
        expect(spy.calledOnce).to.be.true;
        expect(spy.args[0][0]).to.equal('SUM');
        expect(spy.args[0][1]).to.equal(100);
        expect(spy.args[0][2]).to.equal(20);
        spy.restore();
    })
})
