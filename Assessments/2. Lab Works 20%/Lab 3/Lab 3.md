Absolutely! Here’s a **step-by-step guide** for each task in Lab 3 using OpenSSL. This will cover all the commands you need, plus notes on what to screenshot or analyze.

---

## 🔐 **Lab 3: OpenSSL Hands-On Guide**

---

### **Task 1: Symmetric Encryption using AES-256-CBC (3 marks)**

#### 🛠 Steps:
1. **Create a sample file:**
```bash
echo "Mesej rahsia guna AES encryption oleh <Nama Anda>" > rahsia.txt
```

2. **Encrypt the file using AES-256-CBC:**
```bash
openssl enc -aes-256-cbc -salt -in rahsia.txt -out rahsia.txt.enc
```
> You will be prompted to set a password.

3. **Decrypt the file:**
```bash
openssl enc -aes-256-cbc -d -in rahsia.txt.enc -out rahsia_decrypted.txt
```

4. **Verify original vs decrypted:**
```bash
cat rahsia.txt
cat rahsia_decrypted.txt
```

#### 📸 Screenshot:
- Encryption and decryption commands
- `cat` outputs for both files

---

### **Task 2: Asymmetric Encryption using RSA (3 marks)**

#### 🛠 Steps:
1. **Generate RSA private key (2048-bit):**
```bash
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
```

2. **Extract public key:**
```bash
openssl rsa -pubout -in private.pem -out public.pem
```

3. **Create a message file:**
```bash
echo "Ini mesej untuk RSA encryption." > message.txt
```

4. **Encrypt the message with public key:**
```bash
openssl rsautl -encrypt -inkey public.pem -pubin -in message.txt -out message.enc
```

5. **Decrypt with private key:**
```bash
openssl rsautl -decrypt -inkey private.pem -in message.enc -out message_decrypted.txt
```

6. **Verify decrypted content:**
```bash
cat message.txt
cat message_decrypted.txt
```

#### 📸 Screenshot:
- Key generation and encryption/decryption commands
- Content comparison via `cat`

---

### **Task 3: Hashing and Message Integrity using SHA-256 (3 marks)**

#### 🛠 Steps:
1. **Create file:**
```bash
echo "Nama & ID Pelajar" > data.txt
```

2. **Generate SHA-256 hash:**
```bash
openssl dgst -sha256 data.txt
```

3. **Modify file:**
```bash
echo "Modified!" >> data.txt
```

4. **Generate hash again:**
```bash
openssl dgst -sha256 data.txt
```

#### 📸 Screenshot:
- Hash before and after file change

#### 🧠 Explain:
> Hashes change because even a 1-bit difference in input changes the hash entirely. This ensures data integrity.

---

### **Task 4: Digital Signatures using RSA & SHA-256 (5 marks)**

#### 🛠 Steps:
1. **Create a new file:**
```bash
echo "Ini fail yang akan ditandatangani." > signed_file.txt
```

2. **Sign the file (SHA-256 digest):**
```bash
openssl dgst -sha256 -sign private.pem -out signed_file.sig signed_file.txt
```

3. **Verify the signature:**
```bash
openssl dgst -sha256 -verify public.pem -signature signed_file.sig signed_file.txt
```

4. **Modify the file and try verification again:**
```bash
echo "Tampered!" >> signed_file.txt
openssl dgst -sha256 -verify public.pem -signature signed_file.sig signed_file.txt
```

#### 📸 Screenshot:
- Signing and both verification attempts

#### 🧠 Explain:
> Verification fails after tampering because the file hash no longer matches the signed hash.

---

## ✅ Final Deliverables Summary:

- **Walkthrough Document (Markdown)** with:
  - Commands used
  - Screenshots
  - Observations & explanations

- **GitHub Repository**:
  - Include `.txt`, `.enc`, `.pem`, `.sig` files
  - Add README.md with brief descriptions

- **Demo**:
  - Live run or show screenshots
  - Discuss real-world relevance (TLS, file security, software signing)

---

Let me know if you’d like me to generate the Markdown walkthrough file or README for GitHub as well!