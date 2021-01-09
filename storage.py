from django.utils.lorem_ipsum import words


books = [
    {'title': words(2, common=False)}
    for _ in range(5)
]
