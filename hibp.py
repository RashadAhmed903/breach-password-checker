import hashlib
import requests

HIBP_RANGE_URL = "https://api.pwnedpasswords.com/range/"


def count_password_breaches(password: str) -> int:
    sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    response = requests.get(HIBP_RANGE_URL + prefix, timeout=10)
    response.raise_for_status()

    for line in response.text.splitlines():
        candidate_suffix, count = line.split(":")
        if candidate_suffix == suffix:
            return int(count)

    return 0