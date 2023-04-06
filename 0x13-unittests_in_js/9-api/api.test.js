const { expect } = require('chai');
const request = require('request');

describe('Test payment system API Server', () => {
  const baseUrl = 'http://localhost:7865';

  it('Request to an existing endpoint', (done) => {
    request.get(baseUrl, (err, response, body) => {
      if (err) {
        done(err);
        return;
      }

      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('Request to /cart/:id endpoint with a valid param', (done) => {
    const id = 12;
    request.get(`${baseUrl}/cart/${id}`, (err, response, body) => {
      if (err) {
        done(err);
        return;
      }

      expect(body).to.equal(`Payment methods for cart ${id}`);
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Request to /cart/:id endpoint with an invalid param', (done) => {
    const id = 'error';
    request.get(`${baseUrl}/${id}`, (err, response, body) => {
      if (err) {
        done(err);
        return;
      }

      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('Request to an unexisting endpoint', (done) => {
    request.get(`${baseUrl}/fake`, (err, response) => {
      if (err) {
        done(err);
        return;
      }

      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});
