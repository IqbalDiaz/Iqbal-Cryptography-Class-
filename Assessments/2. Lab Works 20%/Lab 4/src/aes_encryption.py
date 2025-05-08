from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# AES needs key length of 16, 24, or 32 bytes (128, 192, 256 bits)
key = get_random_bytes(16)  # AES-128
message = "Cryptography Lab by Iqbal Bin Erman, NWS22102310!"

# Padding function (AES block = 16 bytes)
def pad(text):
    pad_len = 16 - len(text) % 16
    return text + chr(pad_len) * pad_len

def unpad(text):
    return text[:-ord(text[-1])]

# Encrypt
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(message).encode())
encoded_cipher = base64.b64encode(ciphertext).decode()

# Decrypt
decoded_cipher = base64.b64decode(encoded_cipher)
decipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(decipher.decrypt(decoded_cipher).decode())

# Results
print("Encrypted (base64):", encoded_cipher)
print("Decrypted:", decrypted)
