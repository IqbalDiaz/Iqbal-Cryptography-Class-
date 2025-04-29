# 📚 Cryptography - CBS 2373

## 📖 Course Information

- **Course Name**: Cryptography
- **Course Code**: CBS 2373
- **References**:
  - William Stallings - *Network Security Essentials*
  - Samuel Bowne
  - Bruce Schneier - *Applied Cryptography*
- **Synopsis**:  
  Introduction to security services based on cryptography including conventional and modern techniques, focusing on confidentiality, integrity, and authentication.

### 🎯 Career Paths
- Cryptographer
- Cryptographic Engineer
- Security Consultant
- Academic Researcher

### 🛠 Skills Development
- Cryptographic Algorithms (e.g., RSA)
- Mathematical Foundations
- Programming Skills (Python) *(not applied in class)*
- Familiarity with Security Protocols (TLS/SSL, IPSec)

---

## 🧩 Overall Modules

| Module | Topic |
| :--- | :--- |
| 1 | Cryptography Concepts and Fundamentals |
| 2 | Substitution Techniques |
| 3 | Transposition Techniques |
| 4 | Symmetric Cryptography |
| 5 | Asymmetric Cryptography |
| 6 | Cryptographic Protocols |

---

# 🛡 Module 1: Cryptography Concepts and Fundamentals

## 🔐 What is Cryptography?

> "Crypto" = Hidden/Secret, "Graphy" = Writing

- Technique for **secure communication**.
- Prevents third-party access.
- Based on confidentiality, integrity, and authentication.

## 🧠 Basic Concepts

- **Encryption/Decryption**:  
  Transform plaintext ⇄ ciphertext using keys.
- **Key**:  
  Used by algorithms for encryption/decryption.
- **Symmetric Cryptography**:  
  Same key for encryption and decryption (e.g., AES, DES).
- **Asymmetric Cryptography**:  
  Public/private key pairs (e.g., RSA, ECC).
- **Hash Functions**:  
  One-way transformation (e.g., SHA-256, MD5).
- **Digital Signatures**:  
  Ensure authenticity and integrity.
- **Cryptographic Protocols**:  
  Secure communication (e.g., TLS/SSL, PGP).
- **Cryptanalysis**:  
  Study of breaking cryptographic techniques.

## 🚨 Types of Attacks
- Brute-force attacks
- Known-plaintext attacks
- Chosen-plaintext attacks

## 🛠 Applications
- Secure web communications (HTTPS)
- File encryption
- Blockchain (e.g., Bitcoin)

---

# 🏛 Classical Cryptography

## 🔁 Substitution Ciphers
- **Caesar Cipher**: Shift letters by a fixed number.
- **Monoalphabetic Cipher**: Consistent replacement.

## 🔀 Transposition Ciphers
- **Rail Fence Cipher**: Diagonal writing.
- **Columnar Transposition Cipher**: Reordering by columns.

## 🔗 Polyalphabetic Ciphers
- **Vigenère Cipher**: Shifting based on keyword.

---

# 🚀 Modern Cryptography

## 🔒 Symmetric Cryptography
- **AES** (128/192/256 bits)

## 🔑 Asymmetric Cryptography
- **RSA** (Public/Private key encryption)
- **ECC** (Smaller keys, strong security)

## 🔎 Hash Functions
- **SHA-256**, **SHA-3**

## 🔁 Key Exchange Protocols
- **Diffie-Hellman Key Exchange**

## ✍️ Digital Signatures
- **DSA** (Digital Signature Algorithm)

## 🌐 Public Key Infrastructure (PKI)
- Issued by trusted Certificate Authorities (e.g., DigiCert, GlobalSign)

## 📡 Cryptographic Protocols
- **TLS/SSL** (Secure Web Communications)

## 🔥 Cryptanalysis and Security
- Protection against brute-force, side-channel, and differential attacks.

---

# 🔥 CIA Triad in Cryptography

| Concept | Purpose | Techniques |
| :--- | :--- | :--- |
| Confidentiality | Protect information from unauthorized access | Encryption (AES, RSA) |
| Integrity | Ensure data is not altered | Hashing (SHA-256), Digital Signatures |
| Availability | Ensure services/data are accessible | Secure protocols (TLS, IPsec) |

### 🆔 Authentication

- **Methods**:
  - Passwords
  - Biometrics
  - Tokens
  - Multi-Factor Authentication (MFA)
- **Techniques**:
  - Digital Signatures
  - PKI
  - Challenge-Response Authentication

---

# ➗ Modular Arithmetic (mod)

## 📘 Basics

Example:  
`37 mod 9 = 1`

### 🔢 Why mod 26?
- Used to **wrap around alphabets** (A=0, ..., Z=25).
- **Range**: 0–25.

### 📝 Sample Problems
- `100 mod 26`
- `126 mod 26`
- `13 mod 26`
- `-5 mod 26`
- `5 + 10 mod 26`
- `13 - 16 mod 26`
- `32 + 46 mod 26`
- `26 + 52 + 78 + 104 + 130 mod 26`
- `26 – 52 – 78 – 104 – 130 mod 26`

---

# 🧩 Example Keyspaces

- **256-bit AES**:  
  `2^256 - 1`
- **2048-bit RSA**:  
  `2^2048 - 1`

---

# 📄 Assignment & Report

## 🕵️‍♂️ Task
- Find a **recent attack** (e.g., Birthday Attack, Man-in-the-Middle).
- **Analyze** how **CIA Triad** (Confidentiality, Integrity, Authentication) is affected.
- **Provide a real-world scenario** explaining the attack.

## 💡 Case Study
- IT security experts use cryptography to ensure:
  - **Confidentiality**
  - **Integrity**
  - **Authentication**

---

# 🧮 Quick Recap: Why Cryptography Matters?

Cryptography secures digital communication, maintains data integrity, and ensures availability in today's highly connected world — from banking to messaging, from blockchain to secure browsing.
