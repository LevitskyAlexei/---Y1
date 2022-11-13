from string import ascii_lowercase,ascii_uppercase, digits
from random import sample
Symbols_ = ascii_uppercase + ascii_lowercase + digits
def get_random_password(n=8) -> str:
    return "".join(sample(Symbols_, n))  # TODO написать функцию генерации случайных паролей


print(get_random_password())
