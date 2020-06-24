import time
from hashlib import sha256
from math import floor


def truncate_otp(otp, expected_length=6):
    """
    :param otp: str
    :param expected_length: int
    :return: str
    """
    return otp[-expected_length:]


def hash_function(key, message):
    """
    :param key: str
    :param message: str
    :return: str
    """
    if not isinstance(key, str):
        key = str(key)
    if not isinstance(message, str):
        message = str(message)
    hashed = sha256((key + message).encode()).hexdigest()
    offset = int(hashed[-1], 16)
    binary = int(hashed[(offset * 2):((offset * 2) + 8)], 16) & 0x7fffffff
    return str(binary)


def generate_otp(otp_secret, otp_expiry=30, otp_length=6, coefficient=None):
    """
    :param otp_secret: str
    :param otp_expiry: int
    :param otp_length: int
    :param coefficient: int
    :return: str
    """
    hash_value = None
    if coefficient is None:
        coefficient = floor(time.time())
    if otp_expiry != 0:
        message = str(floor(int(coefficient) / otp_expiry))
        hash_value = hash_function(otp_secret, message)
    return truncate_otp(hash_value, otp_length)


def generate_secret(otp_length=6, otp_expiry=30):
    """
    :param otp_length: int
    :param otp_expiry: int
    :return: str
    """
    return "{}.{}.hello".format(otp_length, otp_expiry)
