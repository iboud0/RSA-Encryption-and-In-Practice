import sympy
from math import gcd

def generate_prime(bits=1024):
    """Generate a prime number with specified bits"""
    return sympy.randprime(2**(bits-1), 2**bits)

def mod_inverse(e, phi):
    """Calculate modular multiplicative inverse"""
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    _, x, _ = extended_gcd(e, phi)
    return x % phi
