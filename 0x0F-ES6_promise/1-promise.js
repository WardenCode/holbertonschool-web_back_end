function getFullResponseFromAPI(success) {
  return success
    ? Promise.resolve({ status: 200, body: success })
    : Promise.reject(Error('The fake API is not working currently'));
}

export default getFullResponseFromAPI;
