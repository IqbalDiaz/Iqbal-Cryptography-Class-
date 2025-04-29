# 🔒 Module 2: Substitution Techniques  
*Classical Encryption Techniques*  
**CBS 2373 - Cryptography**

---

## 📖 Introduction

- Classical encryption technique: Encrypt plaintext by **substituting** each letter/symbol according to a key.
- Focus of this module:  
  - **Caesar Cipher**
  - **Monoalphabetic Cipher**
- Mentioned (but not deeply focused): Playfair Cipher, Hill Cipher, Vigenère Cipher.

🔗 [Reference: Substitution Cipher - GeeksforGeeks](https://www.geeksforgeeks.org/substitution-cipher/)

---

# 🧠 Substitution Ciphers

## 🏛 Caesar Cipher

- **Julius Caesar** used it — earliest and simplest.
- Replaces each letter by another letter shifted **3 positions**.
- Alphabet wraps around (A → D, B → E, etc.).

### 📋 Algorithm:
- Assign numerical values: A=0, B=1, ..., Z=25.
- Encryption formula:  
  `C = (p + k) mod 26`
- Decryption formula:  
  `P = (c - k) mod 26`

*(where `k` = shift key, usually 3)*

### 🎯 Activities:
- Encrypt and decrypt given ciphertext using Caesar Cipher manually.
- Brute-force decrypt by trying all 25 possible shifts.

### ⚙️ Brute-force Cryptanalysis:
- Encryption/Decryption algorithms are known.
- Only 25 possible keys → easy brute-force attack.
- Plaintext language recognizable.

---

## 🔁 Monoalphabetic Cipher (Affine Cipher)

- **Improvement over Caesar Cipher**: Arbitrary substitution, larger key space (26! > 4 × 10²⁶ keys).
- Brute-force practically impossible due to keyspace size.

### 📋 Affine Cipher Formulas:

- **Encryption**:  
  `E(x) = (a * x + b) mod 26`
- **Decryption**:  
  `D(x) = a⁻¹(x - b) mod 26`

*(where `a` and `b` are keys, and `a⁻¹` is modular multiplicative inverse of `a` mod 26)*

### 🧮 Modular Multiplicative Inverse:

- Find `a⁻¹` such that:  
  `(a * a⁻¹) mod 26 = 1`

> **Example**:  
> If `a = 7`, then `a⁻¹ = 15` (since `7 × 15 mod 26 = 1`).

### 🎯 Activities:
- Calculate modular inverses for different values.
- Encrypt and decrypt messages using Affine Cipher.
- Brute-force attack practice on Affine Cipher.

---

# 🧩 More Advanced Classical Ciphers

## 🗝 Playfair Cipher (Matrix Concept)

- Uses a **5x5 matrix** generated from a keyword.
- I and J are considered the same letter.
- Encrypts **two letters at a time** (digraphs).

**Example**:  
Keyword = `monarchy`

## 🧩 Hill Cipher (Matrix and Linear Algebra)

- Introduced by **Lester Hill (1929)**.
- Uses **matrix multiplication modulo 26** for encryption and decryption.
- Requires calculating the **inverse matrix** modulo 26 for decryption.

**Excel Tip**:  
Use `=MMULT()` function for matrix multiplication.

### 🎯 Activities:
- Encrypt/decrypt using 2x2, 3x3, and 4x4 key matrices.
- Calculate matrix inverses modulo 26.

---

# 🛡 Polyalphabetic Ciphers (Vigenère Cipher)

- Improves over monoalphabetic by **using multiple Caesar Ciphers**.
- The key is a **word** instead of a single number.

### 📋 Process:

- Each letter of plaintext is encrypted using a different Caesar cipher based on the key letter.
- Set of 26 related Caesar ciphers (shifts from 0 to 25).

**Example**:
- **Keyword**: `deceptive`
- **Message**: `we are discovered save yourself`

**Hint**:  
- Key letter controls shift for that letter.
- Cipher table (Vigenère table) used.

### 🎯 Activities:
- Encrypt and decrypt using Vigenère Cipher manually and via table.

---

# 🧩 Combined Ciphers Activity

> Ciphertext:  
> `Xmtkojgjbt xjindnon ja xmtkojbmvkct (wpdgydib xdkczm ntnozhn) ohr rrgdhubplggwm (pgeiywhu ihma)`

**Task**:
- First half: Decrypt using **Caesar cipher**.
- Second half: Use the decrypted last word of the first half as the **key** for **Vigenère cipher**.

---

# 🛠 Lab Works

1. Install Python on Windows.
2. Write a Python program for:
   - Caesar Cipher Encryption & Decryption
   - Monoalphabetic Cipher (Affine) Encryption & Decryption

---

# 📚 Summary

| Cipher | Key Concept | Method |
| :--- | :--- | :--- |
| Caesar Cipher | Fixed shift | Simple substitution |
| Monoalphabetic Cipher | Arbitrary substitution | Larger keyspace |
| Playfair Cipher | Digraph substitution | 5x5 keyword matrix |
| Hill Cipher | Matrix encryption | Modular arithmetic |
| Vigenère Cipher | Multiple shifts | Keyword-controlled substitution |

---

# 🧠 Important Links

- 🔗 [Modulo Calculator Online](https://www.calculators.org/math/modulo.php)
