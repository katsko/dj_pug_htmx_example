from collections import UserList
from django.utils.lorem_ipsum import words


class Books(UserList):

    def __init__(self):
        super(Books, self).__init__()
        self.data = [
            {'id': index, 'title': words(2, common=False)}
            for index in range(1, 6)
        ]

    def filter(self, letters):
        if not letters:
            return self.data
        return [
            book
            for book in self.data
            if book['title'].lower().startswith(letters)
        ]


books = Books()
