# TODO написать функцию генерации случайных паролей

import string
from random import sample


def get_random_password(size) -> str:
    password = sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, size)
    password = "".join(map(str, password))
    return password


print(get_random_password(8))
