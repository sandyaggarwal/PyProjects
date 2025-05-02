from Book import Book
from User import User


class Library:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.users: dict[str, User] = {}

    def add_book(self, book: Book):
        if book.isbn in self.books.keys():
            print(f'Book {book.title} already available in library!')
            return
        self.books[book.isbn] = book
        print(f'Book {book.title} added to library!')

    def remove_book(self, book: Book):
        if book.isbn not in list(self.books.keys()):
            print(f"Book with title {book.title} not available")
            return
        self.books[book.isbn] = None
        print(f'Book {book.title} removed from library!')

    def issue_book(self, book: Book, user: User):
        if book.isbn in list(self.books.keys()) and not book.get_is_borrowed:
            book.set_is_borrowed(True)
            book.set_borrowed_by(user.mobile_no)

    def return_book(self, book: Book):
        book.set_is_borrowed(False)
        book.set_borrowed_by(None)

    def list_books(self):
        if not self.books:
            print('No book available!')
        for book in self.books.values():
            print(book)

    def add_user(self, user: User):
        if user.mobile_no in list(self.users.keys()):
            print(f'User {user.name} with {user.mobile_no} already exist!')
            return
        self.users[user.mobile_no] = user

    def get_user_details(self, mobile_no: str) -> str:
        if mobile_no not in self.users[mobile_no]:
            print("User details not found")
            return
        return self.users[mobile_no]
