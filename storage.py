from django.utils.lorem_ipsum import words


books = [
    {'id': index, 'title': words(2, common=False)}
    for index in range(1, 6)
]
