import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((r) => {
      console.log(`${r[0].body} ${r[1].firstName} ${r[1].lastName}`);
    })
    .catch(() => console.log('Signup system offline'));
}
