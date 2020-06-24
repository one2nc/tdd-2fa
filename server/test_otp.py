from unittest import TestCase
from otp import generate_otp, hash_function


class Test(TestCase):
    def test_generate_otp(self):
        self.assertEqual("1798492015", generate_otp(otp_expiry=30, otp_secret="hello", coefficient=1234))
        self.assertEqual("1628551077", generate_otp(otp_expiry=30, otp_secret="hello", coefficient=0))

    def test_hash_function(self):
        self.assertEqual("364039319", hash_function("hello", "1234"))
        self.assertTrue(hash_function("hello", 1234), msg="parameters should be str")
