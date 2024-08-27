python
import os
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

logger = setup_logging()

class SecurityManager:
    def __init__(self, key):
        self.key = key
    
    def encrypt_data(self, data):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(data) + encryptor.finalize()
        return iv + encrypted_data
    
    def decrypt_data(self, encrypted_data):
        iv = encrypted_data[:16]
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
        return decrypted_data
    
    def hash_password(self, password):
        sha256 = hashlib.sha256()
        sha256.update(password)
        return sha256.hexdigest()

class User:
    def __init__(self, username, roles):
        self.username = username
        self.roles = roles

class RBAC:
    def __init__(self):
        self.permissions = {}
    
    def add_permission(self, role, permission):
        if role not in self.permissions:
            self.permissions[role] = set()
        self.permissions[role].add(permission)
    
    def check_permission(self, user, permission):
        for role in user.roles:
            if permission in self.permissions.get(role, []):
                return True
        return False

# Example setup
key = os.urandom(32)  # 256-bit key
security_manager = SecurityManager(key)
rbac = RBAC()
rbac.add_permission("admin", "read")
rbac.add_permission("admin", "write")
rbac.add_permission("user", "read")

user1 = User("alice", ["user"])
user2 = User("bob", ["admin"])

# Encrypt and store data
data = b"Sensitive Information"
encrypted_data = security_manager.encrypt_data(data)
with open("data.enc", "wb") as f:
    f.write(encrypted_data)

# Decrypt and read data
with open("data.enc", "rb") as f:
    encrypted_data = f.read()
decrypted_data = security_manager.decrypt_data(encrypted_data)
logger.info(f"Decrypted Data: {decrypted_data}")

# Check permissions
if rbac.check_permission(user1, "write"):
    logger.info("User1 has write permission")
else:
    logger.warning("User1 does not have write permission")

if rbac.check_permission(user2, "write"):
    logger.info("User2 has write permission")
else:
    logger.warning("User2 does not have write permission")

# Hash password
password = b"SuperSecretPassword"
hashed_password = security_manager.hash_password(password)
logger.info(f"Hashed Password: {hashed_password}")