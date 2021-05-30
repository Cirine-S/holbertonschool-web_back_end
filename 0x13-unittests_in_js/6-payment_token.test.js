const getPaymentTokenFromAPI = require('./6-payment_token');
const chai = require('chai');

describe('testing using done', function () {
  it('async test', function (done) {
    getPaymentTokenFromAPI(true)
      .then(function (response) {
        chai
          .expect(response)
          .to.deep.equal({ data: 'Successful response from the API' });
        done();
      })
      .catch(function (error) {
        done(error);
      });
  });
});
