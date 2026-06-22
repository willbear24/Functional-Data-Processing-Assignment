class Book:
    '''Represents a book with a title, author, year and checked_out status'''

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False

    def check_out(self):
        self.checked_out = True
        
    def status(self):
        if self.checked_out:
            return "Unavailable"
        else:
            return "Available"

    def return_book(self):
        self.checked_out = False

    def __repr__(self):
        return f"Title: \"{self.title}\", Author: {self.author}, Year: {self.year}, Status: {self.status()}"
        

class EBook(Book):

    def __init__(self, title, author, year, file_size_mb, max_concurrent_checkouts=3):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb
        self.max_concurrent_checkouts = max_concurrent_checkouts
        self.active_checkouts = 0

    def check_out(self):
        """Allow multiple simultaneous checkouts up to a limit."""
        if self.active_checkouts < self.max_concurrent_checkouts:
            self.active_checkouts += 1

    def return_book(self):
        if self.active_checkouts > 0:
            self.active_checkouts -= 1

    def status(self):
        if self.active_checkouts >= self.max_concurrent_checkouts:
            return "Unavailable"
        return "Available"

    def __repr__(self):
        return (
            f"Title: \"{self.title}\", Author: {self.author}, Year: {self.year}, "
            f"Status: {self.status()}, Active checkouts: {self.active_checkouts}/{self.max_concurrent_checkouts}, "
            f"File size: {self.file_size_mb} MB"
        )


class Catalog:

    def __init__(self):
        self.books = []

    def add_book(self, book_or_title, author=None, year=None):
        if isinstance(book_or_title, Book):
            book = book_or_title
        else:
            if author is None or year is None:
                raise ValueError("Provide a Book object or title, author, and year.")
            book = Book(book_or_title, author, year)

        self.books.append(book)
        return book
    
    def search_by_title(self, keyword):
        keyword = keyword.lower()
        return [book for book in self.books if keyword in book.title.lower()]

    def search_by_author(self, author_name):
        author_name = author_name.lower()
        return [book for book in self.books if author_name in book.author.lower()]

    def get_available(self):
        return [book for book in self.books if not book.checked_out]

    def summary(self):
        print("Catalog Summary:")
        if not self.books:
            print("No books in catalog.")
            return

        for book in self.books:
            print(book)


# TEST
catalog = Catalog()
catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))

# Search
results = catalog.search_by_title("python")
print(results)  # Should find "Python Crash Course"

# Check out
catalog.books[0].check_out()
available = catalog.get_available()
print(f"Available: {len(available)} books")

catalog.summary()