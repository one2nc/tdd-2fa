import argparse

import requests
from modules.otp.functions import generate_otp, truncate_otp


def register(url, device_id):
    headers = {
        "Content-Type": "application/json"
    }
    payload = "{\"device_id\": %s}" % device_id
    return requests.post(url="{}/register".format(url),
                         data=payload, headers=headers)


def get_device_secret(url, device_id):
    return requests.get(url="{}/get_secret/{}".
                        format(url, device_id)).json().get("secret")


def is_registered(url, device_id):
    return requests.get(url="{}/is_registered/{}".format(url, device_id))


def generate_device_otp(otp_secret, coefficient=None):
    device_otp = generate_otp(otp_secret=otp_secret, coefficient=coefficient)
    return truncate_otp(otp=device_otp)


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--device-id', type=int, action='store', required=True,
                        help='id of the device')
    parser.add_argument('--server-addr', type=str, action='store',
                        help='server address', default="http://127.0.0.1:5000")
    return parser


if __name__ == '__main__':
    args_parse = get_parser().parse_args()
    is_device_registered = is_registered(url=args_parse.server_addr,
                                         device_id=args_parse.device_id)
    if not is_device_registered.json().get("is_registered"):
        register_device = register(url=args_parse.server_addr,
                                   device_id=args_parse.device_id)
        secret = register_device.json().get("secret")
    else:
        secret = get_device_secret(url=args_parse.server_addr,
                                   device_id=args_parse.device_id)
    print(truncate_otp(otp=generate_otp(otp_secret=secret)))
