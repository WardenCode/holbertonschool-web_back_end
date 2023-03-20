import { createUser, uploadPhoto } from './utils';

async function asyncUploadUser() {
  let result = {
    photo: null,
    user: null,
  };

  try {
    result = {
      photo: await uploadPhoto(),
      user: await createUser(),
    };
  } catch (error) {
    return result;
  }

  return result;
}

export default asyncUploadUser;
