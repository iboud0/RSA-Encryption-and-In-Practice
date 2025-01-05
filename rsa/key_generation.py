import random
from math import gcd
from .utilities import generate_prime, mod_inverse

def generate_keypair(bits=1024):
    """Generate public and private key pairs"""
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q:
        q = generate_prime(bits)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537
    while gcd(e, phi) != 1:
        e = random.randrange(3, phi, 2)
    
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))
