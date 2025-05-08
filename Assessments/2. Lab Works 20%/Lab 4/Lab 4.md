# 🧪 Lab 4: Implementing Cryptography with Python

---

## 📌 Task 1: Symmetric Encryption (AES)

### ✅ Objective

Use AES (Advanced Encryption Standard) to:

1. Encrypt a message.
2. Decrypt the message back.

---

### 🛠️ Setup

Install the required library:

```bash
pip install pycryptodome
```

---

### 📜 Code

```python
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
```

---

### 📷 Screenshot

Take a screenshot of:

* Encrypted output
* Decrypted output

---

### 🔍 Result Analysis

* AES is **fast and secure** for local encryption.
* ECB mode is **not secure** for real-world use – but okay for learning.
* The same key must be kept secret.

---

## 📌 Task 2: Asymmetric Encryption (RSA)

### ✅ Objective

Use RSA to:

1. Generate key pairs.
2. Encrypt a message using public key.
3. Decrypt using private key.

---

### 🛠️ Setup

```bash
pip install pycryptodome
```

---

### 📜 Code

```python
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
```

---

### 📷 Screenshot

Take a screenshot showing:

* Encrypted message
* Decrypted message

---

### 🔍 Result Analysis

* RSA is used for **secure communication**.
* Public key = encrypt, Private key = decrypt.
* Key size affects security (2048 bits = strong).

---

## 📌 Task 3: Hashing (SHA-256)

### ✅ Objective

Use SHA-256 to:

1. Hash a message.
2. See how small input changes change the hash.

---

### 📜 Code

```python
import hashlib

msg1 = "Hello, world!"
msg2 = "hello, world!"  # small difference

hash1 = hashlib.sha256(msg1.encode()).hexdigest()
hash2 = hashlib.sha256(msg2.encode()).hexdigest()

print("Message 1:", msg1)
print("SHA-256:", hash1)
print("Message 2:", msg2)
print("SHA-256:", hash2)
```

---

### 📷 Screenshot

Take a screenshot showing:

* Both messages
* Both hash outputs

---

### 🔍 Result Analysis

* Even small changes produce a **completely different hash** (avalanche effect).
* SHA-256 is **one-way**, **irreversible**, and used in blockchain, passwords, etc.

---

## 📌 Task 4: Digital Signatures (RSA)

### ✅ Objective

1. Sign a message using private key.
2. Verify using public key.

---

### 📜 Code

```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA keys (or reuse from Task 2)
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Message to be signed
message = b"Digital signature test by Iqbal Bin Erman"

# Hash the message
hash_msg = SHA256.new(message)

# Sign using private key
private = RSA.import_key(private_key)
signer = pkcs1_15.new(private)
signature = signer.sign(hash_msg)

# Verify using public key
public = RSA.import_key(public_key)
verifier = pkcs1_15.new(public)
try:
    verifier.verify(hash_msg, signature)
    print("✅ Signature successfully verified.")
except (ValueError, TypeError):
    print("❌ Signature verification failed.")
```

---

### 📷 Screenshot

Take a screenshot of:

* Signature process
* Successful verification message

---

### 🔍 Result Analysis

* Ensures message **authenticity** and **integrity**.
* Only the holder of the private key can sign.
* Anyone with public key can verify.

