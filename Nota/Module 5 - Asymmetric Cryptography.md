# 🔐 Module 5: Asymmetric Cryptography

## 🎯 Objective
- Understand **principles** of modern asymmetric ciphers like **RSA**.
- Practice:
  - 🛠️ Generate public/private keys
  - 🧮 Calculate message digest

---

## 🔑 What is Asymmetric Cryptography?
- Also known as **public-key cryptography**.
- **Uses two keys**:
  - 🧷 **Public Key**: Shared openly, used for encryption.
  - 🔒 **Private Key**: Secret, used for decryption and signing.

### 🔄 Operations
- Encrypt with 🔑 public → Decrypt with 🔒 private.
- Sign with 🔒 private → Verify with 🔑 public.

---

## 🧩 Key Concepts
- 🔗 **Key Pairs** are mathematically related.
- 📜 **Digital Signatures** verify sender identity and message integrity.
- 🛡️ **Security** depends on trusted **Certificate Authorities (CAs)**.

---

## 🌎 Applications
- 🌐 Secure Communication (SSL/TLS, SSH)
- ✍️ Digital Signatures for contracts and documents
- 🔑 Secure Key Management
- ⚡ Key Examples: RSA, DSA, ECC

---

## 📈 Public Key Algorithms
| Algorithm | Key Principle | Usage |
|:--|:--|:--|
| RSA 🔑 | Factoring large integers | Encryption, Digital Signatures |
| DSA 🖊️ | Discrete logarithm problem | Digital Signatures |
| ECDSA 📈 | Elliptic curves | Mobile systems, Digital Signatures |
| DH 🔄 | Key exchange | Secure key agreement |
| ElGamal 📬 | Discrete logs | Encryption and Signatures |

---

# 📚 RSA Focus

## 📋 Mathematical Foundation
- 🧮 **Euler's Theorem**, **Bézout Theorem**, **GCD Concepts**.
- Encryption/Decryption formulas:
  - Encryption: `C = M^e mod n`
  - Decryption: `M = C^d mod n`
- `d` is found using modular multiplicative inverse.

---

## 🔨 RSA Key Generation (Example)
1. Pick primes: `p = 11`, `q = 3`
2. Compute:
   - `n = p × q = 33`
   - `φ(n) = (p-1)(q-1) = 20`
3. Select `e = 3` (gcd(3,20)=1)
4. Find `d` such that `(e × d) mod φ(n) = 1`
   - Here, `d = 7`
5. Public Key = `(e=3, n=33)`
6. Private Key = `(d=7, n=33)`

---

## 🚀 Encryption Example
- Plaintext: `M = 5`
- Ciphertext: `C = M^e mod n = 5^3 mod 33 = 26`
- Decryption: `M = C^d mod n = 26^7 mod 33 = 5`

---

# ✍️ Digital Signatures

## 📋 Process
1. Sign message with 🔒 private key.
2. Verify using 🔑 public key.

## 🎯 Purpose
- 📜 **Authentication**: Validates sender identity.
- 🔏 **Integrity**: Ensures message is unaltered.
- 🚫 **Non-repudiation**: Sender can't deny sending.

---

## 🔥 Applications
- 💳 Electronic transactions
- 📦 Software distribution
- 📝 Digital document signing (PDF, Emails)

---

# 🧮 Activity: Message Digest (SD11)

## 📋 Steps
1. Convert letters to numbers:
   - A=1, B=2, ..., Z=26
2. Sum the numbers.
3. Take modulo 11 of the sum.

### ✏️ Example: "ELECTRONIC COMMERCE"
- Converted numbers: `5, 12, 5, 3, 20, ...`
- Sum: `179`
- Digest: `179 mod 11 = 3`

---

# 🛠️ Practice
- Practice SD11 on "ALICE" ➡️ Digest = `8`
- Try it on "BOB"!

