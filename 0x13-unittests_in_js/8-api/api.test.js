const request = require('request');
const chai = require('chai')

describe('API test', () => {
      it('respond with 200 code and body', (done) => {
        request('http://localhost:7865', 'GET', (err, res, body) => {
          if (err) throw err;
          chai.expect(res.statusCode).to.equal(200);
          chai.expect(body).to.equal('Welcome to the payment system');
        });
        done();
    });
});
