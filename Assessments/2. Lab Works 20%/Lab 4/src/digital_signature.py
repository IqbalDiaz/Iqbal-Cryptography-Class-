from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

def generate_keys():
    """Generate RSA key pair"""
    key = RSA.generate(2048)
    return key.export_key(), key.publickey().export_key()

def get_message():
    """Get message input from user"""
    choice = input("Use default message? (y/n): ").lower()
    if choice == 'y':
        return b"Digital signature test by Iqbal Bin Erman"
    else:
        return input("Enter your message: ").encode()

def sign_message(private_key, message):
    """Sign a message using private key"""
    hash_msg = SHA256.new(message)
    private = RSA.import_key(private_key)
    signer = pkcs1_15.new(private)
    return signer.sign(hash_msg)

def verify_signature(public_key, message, signature):
    """Verify signature using public key"""
    hash_msg = SHA256.new(message)
    public = RSA.import_key(public_key)
    verifier = pkcs1_15.new(public)
    try:
        verifier.verify(hash_msg, signature)
        return True
    except (ValueError, TypeError):
        return False

def main():
    print("\n" + "="*50)
    print("DIGITAL SIGNATURE DEMO".center(50))
    print("="*50 + "\n")

    # Generate or load keys
    key_choice = input("Generate new keys? (y/n): ").lower()
    if key_choice == 'y':
        private_key, public_key = generate_keys()
        print("\n🔑 New RSA key pair generated")
    else:
        # In a real implementation, you would load from files here
        private_key, public_key = generate_keys()
        print("\n⚠️  Using newly generated keys (file loading not implemented)")

    # Get message
    message = get_message()

    # Sign the message
    signature = sign_message(private_key, message)
    encoded_signature = base64.b64encode(signature).decode()

    # Display signature info
    print("\n" + "-"*50)
    print(f"Original message: {message.decode()}")
    print(f"Message SHA-256: {SHA256.new(message).hexdigest()}")
    print(f"Signature (base64): {encoded_signature}")
    print("-"*50 + "\n")

    # Verify the signature
    print("Verifying signature...")
    if verify_signature(public_key, message, signature):
        print("✅ Signature successfully verified")
    else:
        print("❌ Signature verification failed")

    # Tamper test demonstration
    if input("\nTest with tampered message? (y/n): ").lower() == 'y':
        tampered_msg = message + b" (tampered)"
        print(f"\nTesting with tampered message: {tampered_msg.decode()}")
        if verify_signature(public_key, tampered_msg, signature):
            print("❌ ERROR: Signature verified for tampered message!")
        else:
            print("✅ Correctly rejected tampered message")

if __name__ == "__main__":
    main()