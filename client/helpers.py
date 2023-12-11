import random
import string


def gen_random_word(length: int):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def writer(name: str):
    def write_to_file(data: str):
        with open(name, 'a+') as file:
            file.write(data)

    return write_to_file
