from Crypto.Cipher import AES
from hashlib import sha256
import os

# === 1. Key Recreation ===
KEY_SUFFIX = "RahsiaLagi"
KEY_STR = f"Bukan{KEY_SUFFIX}"
KEY = sha256(KEY_STR.encode()).digest()[:16]  # 16-byte key for AES-128

# === 2. Unpadding Function (PKCS#7) ===
def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

# === 3. Decrypt File ===
def decrypt_file(filepath):
    with open(filepath, "rb") as f:
        ciphertext = f.read()
    cipher = AES.new(KEY, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext)
    
    # Remove ".enc" extension
    original_path = filepath.replace(".enc", "")
    with open(original_path, "wb") as f:
        f.write(plaintext)
    print(f"[+] Decrypted: {original_path}")

# === 4. Process Encrypted Files ===
if __name__ == "__main__":
    folder = "locked_files/"
    for filename in os.listdir(folder):
        if filename.endswith(".enc"):
            decrypt_file(os.path.join(folder, filename))
