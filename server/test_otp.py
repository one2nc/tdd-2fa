from unittest import TestCase
from otp import generate_otp, hash_function


class Test(TestCase):
  def test_generate_secret(self):
    self.assertEqual("27597339",
                     generate_otp(otp_length=3, otp_expiry=30,
                                  otp_secret="hello", coefficient="None"))

  def test_hash_function(self):
    self.assertEquals("364039319", hash_function("hello", "1234"))
    self.assertTrue(hash_function("hello", 1234), msg="parameters should be str")
