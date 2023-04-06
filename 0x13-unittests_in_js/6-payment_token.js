const getPaymentTokenFromAPI = (success) => {
  if (!success) return;

  return Promise.resolve({
    data: 'Successful response from the API',
  });
};

module.exports = getPaymentTokenFromAPI;
