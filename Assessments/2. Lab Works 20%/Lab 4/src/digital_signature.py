from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA keys (or reuse from Task 2)
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Message to be signed
message = b"Digital signature test by Iqbal Bin Erman"

# Hash the message
hash_msg = SHA256.new(message)

# Sign using private key
private = RSA.import_key(private_key)
signer = pkcs1_15.new(private)
signature = signer.sign(hash_msg)

# Verify using public key
public = RSA.import_key(public_key)
verifier = pkcs1_15.new(public)
try:
    verifier.verify(hash_msg, signature)
    print("✅ Signature successfully verified.")
except (ValueError, TypeError):
    print("❌ Signature verification failed.")
