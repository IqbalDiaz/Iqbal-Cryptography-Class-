from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_rsa_keys():
    """Generate and return RSA key pair"""
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def save_keys_to_files(private_key, public_key):
    """Save keys to PEM files"""
    with open("private.pem", "wb") as f:
        f.write(private_key)
    with open("public.pem", "wb") as f:
        f.write(public_key)
    print("Keys saved to private.pem and public.pem")

def get_user_message():
    """Prompt user for message choice"""
    choice = input("Use default message? (y/n): ").lower()
    if choice == 'y':
        return "RSA Encryption Test Message"
    else:
        return input("Enter your message to encrypt: ")

def main():
    print("\n" + "="*50)
    print("Hash Comparison DEMO".center(50))
    print("="*50)
    # Generate keys
    private_key, public_key = generate_rsa_keys()
    
    # Option to save keys to files
    save_choice = input("Save keys to files? (y/n): ").lower()
    if save_choice == 'y':
        save_keys_to_files(private_key, public_key)
    
    # Get message to encrypt
    message = get_user_message()
    
    # Encrypt with public key
    public = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(public)
    encrypted = cipher_rsa.encrypt(message.encode())
    encoded_encrypted = base64.b64encode(encrypted).decode()
    
    # Decrypt with private key
    private = RSA.import_key(private_key)
    decipher_rsa = PKCS1_OAEP.new(private)
    decrypted = decipher_rsa.decrypt(base64.b64decode(encoded_encrypted)).decode()
    
    # Display results
    print("\n=== RSA Encryption Results ===")
    print(f"Original message: {message}")
    print(f"Message length: {len(message)} bytes")
    print(f"Encrypted (base64): {encoded_encrypted}")
    print(f"Encrypted length: {len(encoded_encrypted)} characters")
    print(f"Decrypted message: {decrypted}")
    print("="*30)
    
    # Verify
    if message == decrypted:
        print("✓ Verification successful - original and decrypted messages match")
    else:
        print("✗ Verification failed - messages don't match")

if __name__ == "__main__":
    main()