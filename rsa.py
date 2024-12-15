import random
from math import gcd

# Generate a random prime number
def generate_prime(bits):
    while True:
        prime = random.getrandbits(bits)
        if is_prime(prime):
            return prime

# Check if a number is prime
def is_prime(num, tests=5):
    if num < 2:
        return False
    for _ in range(tests):
        a = random.randint(2, num - 1)
        if pow(a, num - 1, num) != 1:
            return False
    return True

# Generate RSA keys
def generate_keys(bits=512):
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q:
        q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Compute d
    d = pow(e, -1, phi)

    return (e, n), (d, n)

# Encrypt a message
def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

# Decrypt a message
def decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Example Usage
public_key, private_key = generate_keys()

print("Public Key:", public_key)
print("Private Key:", private_key)

message = "Hello RSA!"
ciphertext = encrypt(message, public_key)
print("Encrypted:", ciphertext)

decrypted_message = decrypt(ciphertext, private_key)
print("Decrypted:", decrypted_message)
