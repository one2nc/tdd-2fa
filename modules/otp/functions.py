import string
import time
from hashlib import sha256
from math import floor
import random


def truncate_otp(otp, expected_length=6):
    return str(otp[-expected_length:])


def hash_function(key, message):
    if not isinstance(key, str):
        key = str(key)
    if not isinstance(message, str):
        message = str(message)
    hashed = sha256((key + message).encode()).hexdigest()
    offset = int(hashed[-1], 16)
    binary = int(hashed[(offset * 2):((offset * 2) + 8)], 16) & 0x7fffffff
    return str(binary)


def generate_otp(otp_secret, otp_expiry=30, coefficient=None):
    hash_value = None
    if coefficient is None:
        coefficient = floor(time.time())

    if otp_expiry != 0:
        message = str(floor(int(coefficient) / otp_expiry))
        hash_value = hash_function(otp_secret, message)
    return hash_value


def generate_secret():
    return ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=16))
