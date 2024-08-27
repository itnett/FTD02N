-- Krypter data ved lagring
INSERT INTO compliance_check (regulation, status)
VALUES (pgp_sym_encrypt('GDPR', 'encryptionKey'), pgp_sym_encrypt('Compliant', 'encryptionKey'));