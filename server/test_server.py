from unittest import TestCase
from server import Config, register_device, validate_device_otp

"""
Config is a dataclass created in server with the following attributes:
device_id: int
otp_expiry: int
otp_length: int
otp_secret: str
"""


class Test(TestCase):
    def test_register_device(self):
        expected_device_list = [Config(1, 29, 4, "4.29.hello")]
        self.assertEqual(expected_device_list, register_device(device_id=1, otp_expiry=29, otp_length=4))

    def test_validate_device_otp(self):
        self.assertTrue(validate_device_otp("90170", Config(1, 9, 5, 'yoda')))
