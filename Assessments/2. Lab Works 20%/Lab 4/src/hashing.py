import hashlib

def calculate_sha256(message):
    """Calculate SHA-256 hash of a message"""
    return hashlib.sha256(message.encode()).hexdigest()

def compare_hashes(hash1, hash2):
    """Compare two hashes and return similarity percentage"""
    matching_chars = sum(1 for a, b in zip(hash1, hash2) if a == b)
    return (matching_chars / len(hash1)) * 100

def main():
    print("\n" + "="*50)
    print("Hash Comparison DEMO".center(50))
    print("="*50)
    # Get user input or use default messages
    choice = input("Use default messages? (y/n): ").lower()
    
    if choice == 'y':
        msg1 = "Hello, world!"
        msg2 = "hello, world!"  # Small difference
    else:
        msg1 = input("Enter first message: ")
        msg2 = input("Enter second message: ")
    
    # Calculate hashes
    hash1 = calculate_sha256(msg1)
    hash2 = calculate_sha256(msg2)
    
    # Compare hashes
    similarity = compare_hashes(hash1, hash2)
    
    # Display results
    print(f"\nMessage 1: '{msg1}'")
    print(f"SHA-256: {hash1}")
    print(f"\nMessage 2: '{msg2}'")
    print(f"SHA-256: {hash2}")
    
    print("\n" + "-"*50)
    print(f"Similarity: {similarity:.2f}% character match in hashes")
    print("-"*50)
    
    if msg1 == msg2:
        print("\nNote: Messages are identical but hashes will always match")
    elif hash1 == hash2:
        print("\nWarning: Different messages produced the same hash (collision)!")
    else:
        print("\nObservation: Tiny message differences create completely different hashes")

if __name__ == "__main__":
    main()