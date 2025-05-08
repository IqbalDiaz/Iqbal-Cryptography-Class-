### 🤝 Working with a Partner – Real-Life Exchange (RSA + Signatures)

---

### 🔐 PART 1: RSA – Secure Messaging with a Partner

#### 👤 Your Side:

1. **Generate RSA keys** and share your public key with your partner:

   ```python
   from Crypto.PublicKey import RSA

   key = RSA.generate(2048)
   private_key = key.export_key()
   public_key = key.publickey().export_key()

   with open("my_public.pem", "wb") as f:
       f.write(public_key)
   with open("my_private.pem", "wb") as f:
       f.write(private_key)
   ```

2. **Send your `my_public.pem`** to your partner (USB, email, Telegram, etc.).

---

#### 👤 Partner Side (Receiver):

3. Your partner **encrypts a message using your public key**:

   ```python
   from Crypto.PublicKey import RSA
   from Crypto.Cipher import PKCS1_OAEP
   import base64

   # Load your public key
   with open("partner_public.pem", "rb") as f:
       public_key = RSA.import_key(f.read())

   message = "Hello Iqbal, this is a secret message!"
   cipher = PKCS1_OAEP.new(public_key)
   encrypted_msg = cipher.encrypt(message.encode())

   with open("message.enc", "wb") as f:
       f.write(encrypted_msg)
   ```

4. **Sends `message.enc` back to you.**

---

#### 👤 Your Side:

5. You **decrypt it with your private key**:

   ```python
   from Crypto.PublicKey import RSA
   from Crypto.Cipher import PKCS1_OAEP

   with open("my_private.pem", "rb") as f:
       private_key = RSA.import_key(f.read())

   with open("message.enc", "rb") as f:
       encrypted = f.read()

   cipher = PKCS1_OAEP.new(private_key)
   decrypted = cipher.decrypt(encrypted)
   print("Decrypted message:", decrypted.decode())
   ```

✅ **You now securely received the secret message!**

---

### ✍️ PART 2: RSA Digital Signature – Verifying a Message

#### 👤 You Sign a Message:

1. Sign a message and send both message + signature:

   ```python
   from Crypto.PublicKey import RSA
   from Crypto.Signature import pkcs1_15
   from Crypto.Hash import SHA256

   message = b"This is a signed message from Iqbal."
   hash_msg = SHA256.new(message)

   with open("my_private.pem", "rb") as f:
       private_key = RSA.import_key(f.read())

   signer = pkcs1_15.new(private_key)
   signature = signer.sign(hash_msg)

   with open("signed_message.txt", "wb") as f:
       f.write(message)
   with open("signature.sig", "wb") as f:
       f.write(signature)
   ```

2. Send `signed_message.txt`, `signature.sig`, and `my_public.pem` to your partner.

---

#### 👤 Partner Verifies Your Signature:

3. Partner verifies the message:

   ```python
   from Crypto.PublicKey import RSA
   from Crypto.Signature import pkcs1_15
   from Crypto.Hash import SHA256

   with open("signed_message.txt", "rb") as f:
       message = f.read()
   with open("signature.sig", "rb") as f:
       signature = f.read()
   with open("partner_public.pem", "rb") as f:
       public_key = RSA.import_key(f.read())

   hash_msg = SHA256.new(message)
   verifier = pkcs1_15.new(public_key)

   try:
       verifier.verify(hash_msg, signature)
       print("✅ Signature verified. Message is authentic.")
   except (ValueError, TypeError):
       print("❌ Signature verification failed!")
   ```

✅ If it prints ✅, your identity is confirmed!

---

### 🔁 Summary of What to Send Between Partners

| File                 | Sender  | Receiver Action                   |
| -------------------- | ------- | --------------------------------- |
| `my_public.pem`      | You     | Partner uses it to encrypt/verify |
| `message.enc`        | Partner | You decrypt with private key      |
| `signed_message.txt` | You     | Partner verifies                  |
| `signature.sig`      | You     | Partner verifies                  |

---

Would you like a ZIP template folder for this partner exchange activity?
