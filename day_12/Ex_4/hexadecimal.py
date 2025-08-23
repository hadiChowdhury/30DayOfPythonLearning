import random
import string


def list_of_hexa_colors():
    hex_chars = string.digits + "abcdef"
    hex_color = "".join(random.choice(hex_chars) for _ in range(8))
    return hex_color