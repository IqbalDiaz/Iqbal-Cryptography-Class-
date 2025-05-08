import hashlib

msg1 = "Hello, world!"
msg2 = "hello, world!"  # small difference

hash1 = hashlib.sha256(msg1.encode()).hexdigest()
hash2 = hashlib.sha256(msg2.encode()).hexdigest()

print("Message 1:", msg1)
print("SHA-256:", hash1)
print("Message 2:", msg2)
print("SHA-256:", hash2)
