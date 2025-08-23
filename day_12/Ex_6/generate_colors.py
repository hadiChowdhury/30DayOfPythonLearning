import random
import string

def generate_colors(color, number):
    colors = []

    if color == 'rgb':
        for _ in range(number):
            first_color = random.randint(0, 255)
            second_color = random.randint(0, 255)
            third_color = random.randint(0, 255)

            rgb_color = 'rgb({},{},{})'.format(first_color, second_color, third_color)

            colors.append(rgb_color)

    elif color == 'hexa':
        hex_chars = string.digits + "abcdef"

        for _ in range(number):
            hex_color = "#" + "".join(random.choice(hex_chars) for _ in range(6))
            colors.append(hex_color)
    return colors

