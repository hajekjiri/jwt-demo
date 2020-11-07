import { readFileSync } from 'fs';
import JWT from 'jsonwebtoken';

const PUBLIC_KEY = readFileSync('../keys/fit.public.key');
const PRIVATE_KEY = readFileSync('../keys/fit.private.key');

const AUDIENCE = 'https://courses.fit.cvut.cz/';

const HOUR = 3600;

// sign
const claims = {
  name: 'John Doe',
  classes: ['BI-HWB', 'BI-PST', 'BI-SI1.2', 'BI-SSB'],
};

const signOptions: JWT.SignOptions = {
  algorithm: 'RS256',
  expiresIn: 24 * HOUR,
  audience: AUDIENCE,
  subject: 'john.doe@fit.cvut.cz',
};

const encoded = JWT.sign(claims, PRIVATE_KEY, signOptions);
console.log(`Encoded token: ${encoded}\n`);

// verify
const verifyOptions: JWT.VerifyOptions = {
  audience: AUDIENCE,
};

try {
  const decoded = JWT.verify(encoded, PUBLIC_KEY, verifyOptions);
  console.log('Verification OK');
  console.log(decoded);
} catch (e) {
  console.log('Verification failed');
  console.log(`${e.name ? e.name : 'Error'}: ${e.message ? e.message : 'Something went wrong'}`);
}
