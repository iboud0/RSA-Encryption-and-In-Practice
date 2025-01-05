from .utilities import mod_inverse

def encrypt(message, public_key):
    """Encrypt a message using public key"""
    e, n = public_key
    msg_int = int.from_bytes(message.encode(), 'big')
    if msg_int >= n:
        raise ValueError("Message is too long for the current key size")
    cipher = pow(msg_int, e, n)
    return cipher

def decrypt(cipher, private_key):
    """Decrypt a cipher using private key"""
    d, n = private_key
    msg_int = pow(cipher, d, n)
    try:
        return msg_int.to_bytes((msg_int.bit_length() + 7) // 8, 'big').decode()
    except UnicodeDecodeError:
        return "Decryption failed"
