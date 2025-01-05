import hashlib
from .utilities import mod_inverse

def sign(message, private_key):
    """Sign a message with the private key"""
    d, n = private_key
    hash_message = hashlib.sha256(message.encode()).hexdigest()
    hash_int = int(hash_message, 16)
    if hash_int >= n:
        raise ValueError("Hash is too large for the current key size")
    signature = pow(hash_int, d, n)
    return signature

def verify(message, signature, public_key):
    """Verify a message's signature using the public key"""
    e, n = public_key
    hash_int = pow(signature, e, n)
    hash_message = hashlib.sha256(message.encode()).hexdigest()
    return hash_int == int(hash_message, 16)
