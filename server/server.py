from dataclasses import dataclass
from otp.otp import generate_secret, generate_otp


@dataclass
class Config:
    device_id: int
    otp_expiry: int
    otp_length: int
    otp_secret: str


def register_device(device_id=1, otp_expiry=30, otp_length=6):
    """
    :param device_id: int
    :param otp_expiry: int
    :param otp_length: int
    :return: List of Config object
    """
    return [Config(device_id, otp_expiry, otp_length,
                   generate_secret(otp_length=otp_length, otp_expiry=otp_expiry))]


def validate_device_otp(expected_otp, device_config):
    """
    :param expected_otp: str
    :param device_config: Config
    :return: Boolean
    """
    actual_otp = generate_otp(
        otp_secret=device_config.otp_secret,
        otp_expiry=device_config.otp_expiry,
        otp_length=device_config.otp_length,
        coefficient=1234)
    return actual_otp == expected_otp
