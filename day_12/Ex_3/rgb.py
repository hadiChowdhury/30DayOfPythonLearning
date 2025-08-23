import random

def rgb_color_gen():
    first_color = random.randint(0, 255)
    second_color = random.randint(0, 255)
    third_color = random.randint(0, 255)

    print('# rgb({},{},{})'.format(first_color, second_color, third_color))
