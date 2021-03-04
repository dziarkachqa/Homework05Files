'''Write funtion random_list(begin: int, end: int, amount: int, exclude: list = None) -> list
that creates and returns list of given amount with randomly selected elements excluding
those that were given in exclude list.'''
import random

random.randint(1, 20)


def random_list(begin: int, end: int, amount: int, exclude: list = None):
    temp_list = []

    for i in range(0, amount):
        random_number = random.randint(begin, end)
        while random_number in exclude:
            random_number = random.randint(begin, end)
        temp_list.append(random_number)

    return temp_list


temp_list = random_list(1, 20, 5, [4, 7, 8, 10, 20, 1])
print(temp_list)
