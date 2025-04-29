# 🔐 Module 6: Cryptographic Protocol

---

## 🎯 Focus
- **Digital Envelope**: 🔑 Caesar Cipher + RSA
- **Digital Signature**: 🖋️ Message Digest + RSA
- **Digital Certificate**: 📜 CA + Digital Signature + RSA

---

# 📚 Contents
- Introduction
- Digital Envelope
- Hash Function & Digital Signature
- Digital Certificate
- Cryptographic Applications

---

# ✨ Introduction
- A **Cryptographic Protocol** secures data at the application level.
- **TLS** (Transport Layer Security) secures web connections (HTTPS).

---

# 📦 Digital Envelope

- Provides **confidentiality** 🛡️.
- Steps:
  1. Generate **Session Key** 🔑 (short key, e.g., Caesar Cipher).
  2. Encrypt **Session Key** with public key encryption (RSA).
  3. Encrypt **Plaintext** using the session key.
  4. Send the **ciphertext** + **encrypted session key (digital envelope)**.

### 📜 Example:
- Public Key (Bob): (3, 33)
- Private Key (Bob): (7, 33)
- Plaintext: `LOVE`
- Session Key (Caesar Cipher key): `3`
- Ciphertext: `ORYH`
- Digital Envelope: `27`

---

# 🖋️ Digital Signature (Authentication & Integrity)

- Provides **authentication** ✅ and **message integrity** 🛡️.
- Steps:
  1. Hash the plaintext ➡️ **Message Digest**.
  2. Encrypt the message digest with sender's **private key** (RSA).
  3. Send plaintext + digital signature.

### 📜 Example:
- Plaintext: `ALICE`
- Public Key (Alice): (3, 33)
- Private Key (Alice): (7, 33)
- MD(ALICE): `8`
- Digital Signature: `2`

### 🛠️ Verifying:
- Decrypt the signature using Alice's public key ➡️ recover MD.
- Hash the received plaintext.
- Compare both message digests. ✅

---

# 🧩 Hash Function vs Cryptographic Hash Function

| 🔎 Feature              | 🧮 Hash Function  | 🔐 Cryptographic Hash Function |
|--------------------------|------------------|--------------------------------|
| Collision Resistance     | No ❌            | Yes ✅                        |
| Security                 | Low 🔻            | High 🔺                       |
| Examples                 | Simple hashing   | MD5, SHA-1, SHA-2, SHA-3       |

### 💥 Collisions:
- Hashing two different inputs may give same output.
- MD5 collisions discovered in **2004**.

---

# 📜 Digital Certificate (Authentication)

- Proves the **ownership** of a public key.
- Issued by a **Certificate Authority (CA)** (e.g., Trent).
- Components:
  - Subject identity (owner).
  - Public key.
  - CA's digital signature.

### 🔑 Flow:
1. Alice generates (AKb, AKv).
2. Alice presents her public key to Trent.
3. Trent issues a **digital certificate** by signing Alice's public key.
4. Alice sends her plaintext + digital certificate + digital signature to Bob.
5. Bob verifies:
   - Decrypt certificate using CA's public key.
   - Verify Alice’s public key.
   - Verify digital signature.

---

# ⚡ Lab Activities

- 🔥 **Confidentiality Lab**:  
  - Create Python program for **digital envelope** (Caesar Cipher + RSA).

- 🔥 **Authentication & Integrity Lab**:  
  - Create Python program for **digital signature** + **digital certificate** using SD11 and RSA.

---

# 📝 Key Formulas

### Digital Envelope:
```
DigitalEnvelope = (SessionKey^PublicKeyExponent) mod PublicKeyModulus
```

### Digital Signature:
```
DigitalSignature = (MessageDigest^PrivateKeyExponent) mod PrivateKeyModulus
```

### Verifying Signature:
```
DecryptedMD = (DigitalSignature^PublicKeyExponent) mod PublicKeyModulus
```

---

# 📌 Summary

| 🛡️ Protection Type    | 🔑 Technique Used                   |
|------------------------|-------------------------------------|
| Confidentiality         | Digital Envelope (Session Key + RSA) |
| Authentication          | Digital Signature (Hash + RSA)     |
| Integrity               | Hash Functions                    |
| Certificate Validation  | Digital Certificate (CA + RSA)     |
