from unittest import TestCase
from server.controller import app
from modules.otp.functions import generate_secret, generate_otp, truncate_otp


class Test(TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        self.app.testing = True
        self.device_id = 1
        self.response = self.register()

    def tearDown(self):
        pass

    def register(self):
        return self.app.post("/register", json={"device_id": self.device_id})

    def test_register(self):
        self.assertEqual(True, self.response.json.get("registered"))
        self.assertEqual(200, self.response.status_code)

    def test_is_registered(self):
        response = self.app.get("/is_registered/{}".format(self.device_id))
        self.assertEqual(True, response.json.get("is_registered"))
        self.assertEqual(200, response.status_code)

    def test_validate_otp(self):
        otp = truncate_otp(otp=generate_otp(otp_expiry=30, otp_secret=self.response.json.get("secret")))
        response = self.app.get("/validate/{}".format(self.device_id), json={"OTP": otp})
        self.assertEqual(True, response.json.get("is_valid"))

