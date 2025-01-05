from rsa import generate_keypair, encrypt, decrypt, sign, verify

def main():
    public_key, private_key = generate_keypair(bits=1024)
    print(f"Public Key (e,n): {public_key}")
    print(f"Private Key (d,n): {private_key}")
    
    message = "Messi is the best player in the world"
    print(f"\nOriginal message: {message}")
    
    cipher = encrypt(message, public_key)
    print(f"Encrypted (cipher): {cipher}")
    
    decrypted = decrypt(cipher, private_key)
    print(f"Decrypted message: {decrypted}")
    
    signature = sign(message, private_key)
    print(f"Signature: {signature}")
    
    is_verified = verify(message, signature, public_key)
    print(f"Signature Verified: {is_verified}")

if __name__ == "__main__":
    main()
