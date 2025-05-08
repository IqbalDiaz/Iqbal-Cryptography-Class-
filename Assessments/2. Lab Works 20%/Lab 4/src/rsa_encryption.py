from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generate RSA key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Save keys to files (optional)
with open("private.pem", "wb") as f:
    f.write(private_key)
with open("public.pem", "wb") as f:
    f.write(public_key)

# Encrypt with public key
public = RSA.import_key(public_key)
cipher_rsa = PKCS1_OAEP.new(public)
message = "RSA Encryption Test Message"
encrypted = cipher_rsa.encrypt(message.encode())
encoded_encrypted = base64.b64encode(encrypted).decode()

# Decrypt with private key
private = RSA.import_key(private_key)
decipher_rsa = PKCS1_OAEP.new(private)
decrypted = decipher_rsa.decrypt(base64.b64decode(encoded_encrypted)).decode()

# Results
print("Encrypted (base64):", encoded_encrypted)
print("Decrypted:", decrypted)
