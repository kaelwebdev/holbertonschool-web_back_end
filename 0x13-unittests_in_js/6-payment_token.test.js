const { expect } = require('chai');
const getPaymentTokenFromApi = require('./6-payment_token.js');

describe('getPaymentTokenFromAPI', () => {
    it('true is passed', (done) => {
        getPaymentTokenFromApi(true).then(function(r) {
            expect(r).to.eql({ data: 'Successful response from the API' })
            done();
        }).catch((err) => {
            done(err);
        });
    })
})
