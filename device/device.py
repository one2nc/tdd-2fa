import argparse

import requests
from modules.otp.functions import generate_otp, truncate_otp


def register(url, device_id):
    headers = {
        "Content-Type": "application/json"
    }
    payload = "{\"device_id\": %s}" % device_id
    return requests.post(url="{}/register".format(url), data=payload, headers=headers)


def is_registered(url, device_id):
    return requests.get(url="{}/is_registered/{}".format(url, device_id))


def generate_device_otp(otp_secret, coefficient=None):
    device_otp = generate_otp(otp_secret=otp_secret, coefficient=coefficient)
    return truncate_otp(otp=device_otp)
