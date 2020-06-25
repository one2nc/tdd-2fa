from unittest import TestCase
from modules.otp.functions import generate_otp, hash_function, truncate_otp, generate_secret


class Test(TestCase):
    def test_generate_otp(self):
        self.assertEqual("1798492015", generate_otp(otp_expiry=30, otp_secret="hello", coefficient=1234))
        self.assertEqual("855156820", generate_otp(otp_expiry=30, otp_secret="hello123", coefficient=0))
        self.assertTrue(isinstance(
            generate_otp(otp_expiry=30, otp_secret="hello", coefficient=1234), str))

    def test_hash_function(self):
        self.assertEqual("364039319", hash_function("hello", "1234"))
        self.assertTrue(hash_function("hello", 1234), msg="parameters should be str")

    def test_truncate_otp(self):
        self.assertEqual("039319", truncate_otp("364039319", expected_length=6))

