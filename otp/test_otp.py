from unittest import TestCase
from otp import generate_otp, hash_function, truncate_otp, generate_secret


class Test(TestCase):
    def test_generate_otp(self):
        self.assertEqual("92015", generate_otp(otp_expiry=30, otp_secret="hello", otp_length=5, coefficient=1234))
        self.assertEqual("56820", generate_otp(otp_expiry=30, otp_secret="hello123", otp_length=5, coefficient=0))
        self.assertTrue(isinstance(
            generate_otp(otp_expiry=30, otp_secret="hello", otp_length=5, coefficient=1234), str))

    def test_hash_function(self):
        self.assertEqual("364039319", hash_function("hello", "1234"))
        self.assertTrue(hash_function("hello", 1234), msg="parameters should be str")

    def test_truncate_otp(self):
        self.assertEqual("039319", truncate_otp("364039319", expected_length=6))

    def test_generate_secret(self):
        self.assertEqual("4.15.hello", generate_secret(otp_length=4, otp_expiry=15))
