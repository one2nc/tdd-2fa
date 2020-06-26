from server.model import OTP
from modules.otp.functions import generate_secret, generate_otp, truncate_otp

device_list = {}


def register_device(device_id):
    secret = generate_secret()
    otp_config = OTP(30, 6, secret)
    device_list[str(device_id)] = otp_config
    return device_list


def get_device_info(device_id):
    return device_list.get(str(device_id))


def validate_otp(device_id, received_otp):
    otp_config = get_device_info(device_id)
    generated_otp = truncate_otp(
        otp=generate_otp(otp_expiry=otp_config.expiry,
                         otp_secret=otp_config.secret),
        expected_length=otp_config.length)
    return generated_otp == received_otp
