import random
import string

def user_id_gen_by_user():
    id_length = int(input("Enter the number of characters per ID: "))
    id_count = int(input("Enter how many IDs you want to generate: "))

    all_char = string.ascii_letters + string.digits

    for i in range(id_count):
        user_id = ''.join(random.choice(all_char) for _ in range(id_length))
        print("#",user_id)




