# RSA Cryptographic System

## Introduction

This project demonstrates the implementation of an **RSA Cryptographic System** in Python. RSA is a widely used public-key cryptographic algorithm that ensures secure data transmission. The project includes functions for generating keys, encrypting and decrypting messages, and signing and verifying messages.

## Project Structure

- **`rsa/`**
  - **`__init__.py`**: Initializes the module and imports key functions.
  - **`key_generation.py`**: Contains functions for generating public and private key pairs.
  - **`encryption.py`**: Includes functions for encryption and decryption of messages.
  - **`signing.py`**: Provides functionality for signing messages and verifying signatures.
  - **`utilities.py`**: Contains helper functions like `generate_prime` and `mod_inverse`.
- **`main.py`**: Entry point for testing the RSA system with key generation, encryption, signing, and verification.
- **`requirements.txt`**: Contains requirements needed to run the project.
- **`README.md`**: Documentation file (this file).

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/iboud0/RSA-Encryption-and-In-Practice.git
   cd RSA-Encryption-and-In-Practice
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python main.py
   ```

## Key Functions

### `generate_keypair(bits=1024)`
Generates a public and private RSA key pair.
- **Parameters:** `bits` - The number of bits for the key size (default is 1024)
- **Returns:** Tuple containing (public_key, private_key)

### `encrypt(message, public_key)`
Encrypts a message using the RSA public key.
- **Parameters:**
  - `message` - The message to encrypt
  - `public_key` - The public key used for encryption
- **Returns:** Encrypted message (ciphertext)

### `decrypt(cipher, private_key)`
Decrypts a ciphertext using the RSA private key.
- **Parameters:**
  - `cipher` - The encrypted message
  - `private_key` - The private key used for decryption
- **Returns:** Decrypted message (plaintext)

### `sign(message, private_key)`
Signs a message using the RSA private key.
- **Parameters:**
  - `message` - The message to sign
  - `private_key` - The private key used for signing
- **Returns:** Message signature

### `verify(message, signature, public_key)`
Verifies the authenticity of a message's signature.
- **Parameters:**
  - `message` - The original message
  - `signature` - The signature to verify
  - `public_key` - The public key used for verification
- **Returns:** Boolean (True if signature is valid)

## Helper Functions

### `generate_prime(bits=1024)`
Generates a random prime number.
- **Parameters:** `bits` - The number of bits for the prime number (default is 1024)
- **Returns:** A prime number in the range [2^(bits-1), 2^bits]
- **Location:** `utilities.py`

### `mod_inverse(e, phi)`
Calculates the modular multiplicative inverse using Extended Euclidean Algorithm.
- **Parameters:**
  - `e` - The number to find inverse for
  - `phi` - The modulus
- **Returns:** Modular multiplicative inverse of e modulo phi
- **Location:** `utilities.py`

## Program Variables

The main program (`main.py`) uses the following key variables:
- `public_key`: Generated RSA public key
- `private_key`: Generated RSA private key
- `message`: Plaintext message for encryption/signing
- `cipher`: Encrypted message
- `decrypted`: Decrypted message
- `signature`: Message signature
- `is_verified`: Signature verification result

## Requirements

Required Python packages:
- sympy
- hashlib
