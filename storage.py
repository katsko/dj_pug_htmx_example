from keyword import kwlist
from random import choice


books = [
    {'title': ' '.join([choice(kwlist) for _ in range(3)])}
    for _ in range(5)
]
