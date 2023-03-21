import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((promises) => {
    const result = [];
    for (const { status, value, reason } of promises) {
      result.push({
        status,
        value: value || reason.toString(),
      });
    }
    return result;
  });
}

export default handleProfileSignup;
