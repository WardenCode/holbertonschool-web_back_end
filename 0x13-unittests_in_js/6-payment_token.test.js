const getPaymentTokenFromAPI = require('./6-payment_token');
const { expect } = require('chai');

describe('Test getPaymentTokenFromAPI function', () => {
  // Promises Version
  it('Test the succesfully return of the API', (done) => {
    getPaymentTokenFromAPI(true)
      .then((data) => {
        expect(data).to.eql({
          data: 'Successful response from the API',
        });
        done();
      })
      .catch(done);
  });

  // Better Promises Version
  // it('Test the succesfully return of the API', () => {
  //   return getPaymentTokenFromAPI(true).then((data) => {
  //     expect(data).to.eql({
  //       data: 'Successful response from the API',
  //     });
  //   });
  // });

  // Async/Await version
  // it('Test the succesfully return of the API', async () => {
  //   const apiResponse = await getPaymentTokenFromAPI(true);

  //   expect(apiResponse).to.eql({
  //     data: 'Successful response from the API',
  //   });
  // });
});
