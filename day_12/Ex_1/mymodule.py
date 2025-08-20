import random
import string


def random_user_id(length):
    letter = string.ascii_letters
    digits = string.digits

    all_chars = letter + digits

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password