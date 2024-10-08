python
import jwt
import datetime

# Generer en JWT
payload = {
    'user_id': 123,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
}
token = jwt.encode(payload, 'secret_key', algorithm='HS256')
print(token)

# Dekod en JWT
try:
    decoded_payload = jwt.decode(token, 'secret_key', algorithms=['HS256'])
    print(decoded_payload)
except jwt.ExpiredSignatureError:
    print("Token has expired")
except jwt.InvalidTokenError:
    print("Invalid token")