
# 🔍 Ransomware Static Analysis & Reverse Engineering Report

**Author:** Iqbal bin Erman  
**Course:** CBS 2373 Cryptography  
**Test:** Practical Test 2 – Simulated Ransomware Decryption  
**Date:** 24/05/25

---

## 1. 📦 Binary Analysis

### 1.1 Packaging and Language Detection

Using the `file` command and **Detect It Easy (DIE)**, the ransomware binary was identified as a **Python-based executable packaged with PyInstaller**.

```bash
$ file suspicious_binary.exe
Python 3.10 PyInstaller archive
````

---

## 2. 🧬 Reverse Engineering

### 2.1 Extraction and Decompilation

**Tool Used:** `pyinstxtractor.py`

```bash
python pyinstxtractor.py suspicious_binary.exe
```

Output: A folder named `suspicious_binary.exe_extracted` containing `.pyc` files.

**Tool Used:** `uncompyle6`

```bash
uncompyle6 extracted_file.pyc -o .
```

Recovered the source code in Python format.

---

## 3. 🔐 Cryptographic Analysis

### 3.1 Algorithm and Mode Used

From the recovered source code:

```python
from Crypto.Cipher import AES
cipher = AES.new(key, AES.MODE_CBC, iv)
```

* **Algorithm:** AES
* **Mode:** CBC (Cipher Block Chaining)
* **Padding:** PKCS7
* **Block Size:** 128-bit
* **Key Length:** 128-bit (16 bytes)

### 3.2 Hardcoded Key and IV

```python
key = b'0123456789abcdef'
iv = b'fedcba9876543210'
```

Both **key and IV were hardcoded** directly in the source, making the encryption easily reversible.

---

## 4. 🧨 Cryptographic Flaws

### ❌ Identified Issues

| Flaw                  | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| 🔑 Hardcoded Key      | Anyone can decrypt files without brute-force                 |
| ♻️ IV Reuse           | Using the same IV for all files in CBC mode                  |
| 🚫 No Integrity Check | No HMAC or AES-GCM, so tampered ciphertext won't be detected |
| 🔓 No Key Derivation  | Secure derivation methods like PBKDF2 or Argon2 are not used |

---

## 5. 🔓 Key Recovery

The key and IV were **directly hardcoded** in the Python source. No brute-force or advanced recovery needed.

* **Key:** `0123456789abcdef`
* **IV:** `fedcba9876543210`

---

## 6. ✅ Decryption Implementation

A decryption script (`decrypt.py`) was written using `pycryptodome`. It reads `.enc` files, decrypts using AES-CBC and the recovered key/IV, and outputs the original plaintext files.

Tested on multiple encrypted files, all successfully decrypted and verified.

---

## 7. 🛡️ Recommendations

To make this ransomware cryptographically stronger:

| Suggestion                       | Reason                                |
| -------------------------------- | ------------------------------------- |
| 🔒 Use AES-GCM or ChaCha20       | Provides authenticated encryption     |
| 🔑 Derive Key using PBKDF2       | Prevents easy recovery of static keys |
| 🎲 Generate IV randomly per file | Prevents pattern leakage in CBC mode  |
| 🧾 Add HMAC or signature         | Verifies integrity and authenticity   |

---

## 8. 📸 Screenshots

Please see the `/screenshots/` folder for:

* Extraction of PyInstaller archive
* Decompiled code showing key/IV
* Running `decrypt.py` successfully
* Before and after of `.enc` files

---

## 9. 📁 Directory Structure

```plaintext
ransomware-decryptor/
├── decrypt.py
├── analysis.md
├── README.md
├── encrypted/
│   ├── file1.txt.enc
├── decrypted/
│   ├── file1.txt
├── screenshots/
│   ├── pyinstxtractor.png
│   ├── key_recovery.png
│   ├── decryption_success.png
```

---
