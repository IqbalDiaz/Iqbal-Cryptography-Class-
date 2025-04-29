# 🔐 Module 3: Transposition Techniques

## 🔎 Introduction
- **Transposition technique**: Encrypts by **scrambling positions** of characters without altering the characters themselves.
- **Types of Transposition**:
  - 🚂 Rail Fence Transposition
  - 🏛 Columnar Transposition
  - 🛡️ Improved (Double) Columnar Transposition

---

## 🚂 Rail Fence Transposition

### 📋 Steps:
1. Write the plaintext diagonally in a **zigzag**.
2. Read across the rows to get the **ciphertext**.

### ⚡ Important:
- The **key** (number of rails) **must not exceed** the message length.
- If rails ≥ message length → ❌ Encryption fails.

### ✏️ Example:
- **Plaintext**: `meet me tomorrow`
- **Encryption**:
  - Written diagonally (zigzag across rails)
  - Read across rows to get ciphertext

### 🛠️ Activity:
- Use **Excel** to:
  - Encrypt "CODEBREAKING" with different rail numbers.
  - Brute-force decrypt using different rail values.
  - Find best decryption matching the original text.

---

## 🏛 Columnar Transposition

### 📋 Concept:
- Write the plaintext **row by row** into a table.
- **Reorder columns** based on a **numeric key**.
- Read down columns **according to key order** to get ciphertext.

### ✏️ Example:
- **Key**: `4 3 1 2 5 6 7`
- Start reading column with label `1`, then `2`, etc.

### 🛠️ Activity:
- Encrypt and decrypt:
  - Example text: `attack postponed until further notice`
  - Key: `4 1 5 3 2`

---

## 🛡️ Improved (Double) Columnar Transposition

### 📋 Concept:
- Apply **columnar transposition twice**!
- **Result**: Much harder for cryptanalysts to break. 💥

### ✏️ Example:
- After 1st transposition → reordered text.
- After 2nd transposition → even more complex scrambling.

---

## 🧪 Activities & Challenges

- 🛠️ **Excel Activity**:
  - Encrypt and decrypt using Rail Fence Cipher.
- 🐍 **Python Lab**:
  - Program Columnar Transposition encryption and decryption.
- 🧠 **Cryptanalysis**:
  - Find possible keys based on given ciphertexts (e.g., "REATCIGHLANFZIEGQNIUCZEESI").

