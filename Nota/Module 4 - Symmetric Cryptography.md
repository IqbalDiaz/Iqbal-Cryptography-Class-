# 🔐 Module 4: Symmetric Cryptography

## 🎯 Objective
- Understand modern symmetric ciphers (**Stream Cipher & Block Cipher**).
- Focus on **XOR Cipher** for stream ciphers and **Feistel Cipher** for block ciphers.
- Explore **Simplified DES (S-DES)**.

---

## 📚 Contents
- Introduction
- Stream Ciphers
- Block Ciphers
- Feistel Cipher Structure
- Simplified DES (S-DES)

---

# 🌊 Stream Cipher (e.g., RC4)

- Encrypts **one bit/byte** at a time 🔄.
- Combines plaintext with a **pseudo-random keystream** using XOR ➡️.

### 🧩 Key Points:
- **Key Stream Generation**: 🎰 Pseudo-random output from the key.
- **Efficiency**: ⚡ High speed, real-time encryption.
- **Security**: 🛡️ Depends on the secrecy of the keystream.
- **Applications**: 🌐 Internet security, 💽 Disk encryption, 📺 Streaming media.

### 📝 Note:
- Same bits → `0`
- Different bits → `1`

---

# 🧱 Block Cipher (e.g., DES)

- Encrypts **fixed-size blocks** (64/128 bits) 📦 at once.

### 🛠️ Key Points:
- **Block Size**: 64 or 128 bits.
- **Key Size**: 64–256 bits 🔑.
- **Encryption Process**: 🔄 Multiple rounds of substitution, permutation, mixing.
- **Modes of Operation**:
  - 📦 ECB
  - 🔗 CBC
  - 🔢 CTR
  - 🧪 GCM
- **Applications**: 
  - 🔒 TLS/SSL
  - 💽 BitLocker
  - 🛢️ Database encryption

### Examples:
- 🛡️ AES
- 🛡️ DES
- 🛡️ 3DES
- 🛡️ Speck
- 🛡️ Simon

---

# ♻️ Feistel Cipher Structure

- Base for DES and many modern block ciphers 🛠️.

### 🧩 Steps:
1. ✋ Split input into **Left (L)** and **Right (R)**.
2. 🔄 R goes unchanged, L is modified with a **Feistel function (fs)**.
3. 🔁 Swap L and R after each round.

### 🔐 Feistel Encode Algorithm:
1. Divide plaintext → `L0` and `R0`.
2. Apply `fs` to `R0`.
3. Set `L1 = R0`, `R1 = L0 XOR fs(R0)`.
4. Concatenate `L1` and `R1`.

---

# 🧪 Simplified DES (S-DES)

- **Teaching Tool** for encryption basics 🧠.

### 📋 Specifications:
- **Block Size**: 8 bits
- **Key Size**: 10 bits (generates two 8-bit subkeys)
- **Rounds**: 2 rounds 🔄

---

## 🔑 Key Generation:

1. Apply **P10** permutation 🔢.
2. Split into two 5-bit halves ➡️⬅️.
3. **Left-shift** by 1 (LS-1).
4. Apply **P8** permutation to get **K1** 🔐.
5. **Left-shift** by 2 (LS-2).
6. Apply **P8** again to get **K2** 🔐.

---

## 🛡️ Encryption Steps:

1. Perform **Initial Permutation (IP)**.
2. ➡️ Split into two halves.
3. Expand and permute the right half (EP).
4. XOR with **K1**.
5. Apply S-Boxes (S0 & S1) 🧩.
6. Apply **P4** permutation.
7. XOR with the left half.
8. Swap halves 🔄.
9. Repeat with **K2**.
10. Apply **Inverse Initial Permutation (IP⁻¹)**.

---

## 📚 Example:
- 🔑 Key-1 = `10100100`
- 🔑 Key-2 = `01000011`
- 📄 Plaintext = `10010111`
- 📜 Ciphertext = `00111000`

---

# 🧠 Activities

- ✅ Encrypt/Decrypt using XOR Cipher.
- ✅ Encode/Decode with Feistel Cipher.
- ✅ Encrypt using S-DES.

