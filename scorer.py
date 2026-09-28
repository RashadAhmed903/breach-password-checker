import math
import string

GUESSES_PER_SECOND = 10_000_000_000
MAX_ENTROPY_BITS = 200


def estimate_entropy_bits(password: str) -> float:
    pool_size = 0

    if any(char in string.ascii_lowercase for char in password):
        pool_size += 26
    if any(char in string.ascii_uppercase for char in password):
        pool_size += 26
    if any(char in string.digits for char in password):
        pool_size += 10
    if any(char in string.punctuation for char in password):
        pool_size += 32

    if pool_size == 0:
        return 0.0

    return len(password) * math.log2(pool_size)


def estimate_crack_seconds(entropy_bits: float) -> float:
    capped_bits = min(entropy_bits, MAX_ENTROPY_BITS)
    return (2 ** capped_bits) / 2 / GUESSES_PER_SECOND


def rate_password(entropy_bits: float) -> str:
    if entropy_bits < 28:
        return "very weak"
    if entropy_bits < 36:
        return "weak"
    if entropy_bits < 60:
        return "fair"
    if entropy_bits < 80:
        return "strong"
    return "very strong"