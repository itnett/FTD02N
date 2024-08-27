const crypto = require('crypto');
const algorithm = 'aes-256-ctr';
const secretKey = 'mysecretkey';
const iv = crypto.randomBytes(16);

const encrypt = (text) => {
  const cipher = crypto.createCipheriv(algorithm, secretKey, iv);
  const encrypted = Buffer.concat([cipher.update(text), cipher.final()]);
  return `${iv.toString('hex')}:${encrypted.toString('hex')}`;
};

const encryptedText = encrypt('Sensitive data');
console.log(encryptedText);