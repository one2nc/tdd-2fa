from dataclasses import dataclass


@dataclass
class OTP:
    expiry: int
    length: int
    secret: str
