import random

def generate_random_list():
    random_list = []
    for i in range(10):
        random_list.append(random.randint(10, 20))
    return random_list
def list():
    my_list = generate_random_list()
    print(my_list)

list();
