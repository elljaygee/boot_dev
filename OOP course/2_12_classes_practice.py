class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        books_keep = []
        for item in self.books:
            title_match = item.title == book.title
            author_match = item.author == book.author
            if not (title_match and author_match):
                books_keep.append(item)
        self.books = books_keep

    def search_books(self, search_string):
        books_matched = []
        query = search_string.lower()
        for item in self.books:
            if query in item.title.lower() or query in item.author.lower():
                books_matched.append(item)

        return books_matched
