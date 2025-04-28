# 🔐 **Lab 3 Summary: Exploring Cryptographic Tools – Hashing, Encryption & Digital Signatures**

---

## 🎯 **Objectives**
- Learn how to use **OpenSSL** to perform key cryptographic operations.
- Understand and apply:
  - **Symmetric encryption** (AES-256-CBC)
  - **Asymmetric encryption** (RSA)
  - **Hashing** (SHA-256)
  - **Digital signatures** (RSA with SHA-256)

By the end of this lab, you will be able to:
- Encrypt and decrypt files using symmetric and asymmetric encryption.
- Generate and verify file hashes to ensure integrity.
- Create and verify digital signatures for authenticity.

---

## 🛠️ **Lab Tasks**

---

### 🔒 Task 1: Symmetric Encryption and Decryption (AES-256-CBC)

**Scenario:**  
Labu wants to send a confidential message to Labi. You will encrypt and decrypt the message using AES-256-CBC.

✅ **Security Note:**  
- AES-256-CBC is used for simplicity. In real-world scenarios, prefer authenticated encryption (e.g., AES-GCM).

**What You'll Do:**
- Generate a strong random AES key.
- Encrypt a text file (e.g., `<Your Name>.txt`) using OpenSSL and AES-256-CBC.
- Decrypt the ciphertext using the same key.
- Verify the decrypted file matches the original.

---

### 🔑 Task 2: Asymmetric Encryption and Decryption (RSA)

**Scenario:**  
Labi wants to securely receive messages from Labu. You will use RSA encryption.

✅ **Security Note:**  
- RSA keys must be at least **2048 bits** for strong security.

**What You'll Do:**
- Generate a 2048-bit RSA private key.
- Extract the corresponding public key.
- Encrypt a secret message (`rahsia.txt`) using the public key.
- Decrypt it using the private key.
- Verify the decrypted content matches the original.

---

### 🔗 Task 3: Hashing and Integrity Verification (SHA-256)

**Scenario:**  
Labu wants to verify document integrity before sending it to Labi.

**What You'll Do:**
- Create a text file (e.g., `<Your Name>.txt`).
- Generate a SHA-256 hash of the file using OpenSSL.
- Modify the file slightly.
- Generate a new hash and compare both hashes.
- Observe and explain how even small changes affect the hash.

✅ **Alternative Tools:**  
- You may explore both `openssl dgst -sha256` and `sha256sum`, but OpenSSL is the primary requirement.

---

### 🖊️ Task 4: Digital Signatures (RSA with SHA-256)

**Scenario:**  
Labu wants to digitally sign a document for Labi to verify.

**What You'll Do:**
- Use your RSA private key to sign a file (e.g., `agreement.txt`) using OpenSSL and SHA-256.
- Verify the signature using the public key.
- Modify the file and test signature verification again.
- Observe and explain why verification fails after tampering.

