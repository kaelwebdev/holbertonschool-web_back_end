import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const signIn = await signUpUser(firstName, lastName)
    .then((r) => ({
      status: 'fulfilled',
      value: r,
    }))
    .catch((e) => ({
      status: 'rejected',
      value: e.toString(),
    }));
  const upload = await uploadPhoto(fileName)
    .catch((e) => ({
      status: 'rejected',
      value: e.toString(),
    }));
  return [signIn, upload];
}
