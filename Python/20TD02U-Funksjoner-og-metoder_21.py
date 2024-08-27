python
     def secure_login(username, password):
         hashed_password = hash_password(password)
         # Valider brukernavn og passord
         return validate_credentials(username, hashed_password)