import random

def list_of_rgb_colors(number):
    rgb_list = []
    for _ in range(number):

        first_color = random.randint(0, 255)
        second_color = random.randint(0, 255)
        third_color = random.randint(0, 255)

        rgb_color = 'rgb({},{},{})'.format(first_color, second_color, third_color)

        rgb_list.append(rgb_color)

    return rgb_list

        # print('# rgb({},{},{})'.format(first_color, second_color, third_color))
