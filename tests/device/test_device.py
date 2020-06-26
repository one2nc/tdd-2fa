from multiprocessing import Process
from unittest import TestCase
from device.device import register, is_registered, generate_device_otp
from server.controller import app


class Test(TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5000"
        self.device_id = 1
        with app.app_context():
            app.env = "Testing"
            self.server_process = Process(target=app.run)
            self.server_process.start()
            self.register_resp = register(url=self.url, device_id=self.device_id)

    def tearDown(self):
        self.server_process.terminate()

    def test_register(self):
        self.assertEqual(True, self.register_resp.json().get("registered"))
        self.assertEqual(200, self.register_resp.status_code)

    def test_is_registered(self):
        is_registered_resp = is_registered(self.url, self.device_id)
        self.assertEqual(True, is_registered_resp.json().get("is_registered"))
        self.assertEqual(200, is_registered_resp.status_code)

    def test_generate_device_otp(self):
        otp_secret = "MLI30O3KJLYWMHO5"
        self.assertEqual("201717", generate_device_otp(otp_secret=otp_secret, coefficient=1234))
