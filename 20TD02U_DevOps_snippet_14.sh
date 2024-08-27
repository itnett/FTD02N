# Lagre en hemmelighet
   vault kv put secret/myapp db_password=secret

   # Hent en hemmelighet
   vault kv get -field=db_password secret/myapp