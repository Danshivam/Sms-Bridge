import re


def extract_otp(message: str):

    match = re.search(r"\b\d{4,8}\b", message)

    if match:
        return match.group()

    return None