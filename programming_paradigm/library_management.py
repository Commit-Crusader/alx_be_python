class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self_is_checked_out = False

    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f'{book.title} by {book.author}')

    def check_out_book(self, title):
        for book in self._books:
            if book.is_available() and book.title == title:
                book.check_out()

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
