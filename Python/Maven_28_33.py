python
   from cryptography.fernet import Fernet

   key = Fernet.generate_key()
   cipher_suite = Fernet(key)
   kryptert_data = cipher_suite.encrypt(b"Sensitiv informasjon")