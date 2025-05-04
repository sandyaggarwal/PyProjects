from Book import Book
from User import User


class Library:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.users: dict[str, User] = {}

    def add_book(self, book: Book):
        if book.isbn in self.books:
            print(f'Book {book.title} already available in library!')
            return
        self.books[book.isbn] = book
        print(f'Book: ({book.title}) -> added to library!')

    def remove_book(self, book: Book):
        if book.isbn not in self.books:
            print(f"Book with title {book.title} not available")
            return
        del self.books[book.isbn]
        print(f'Book {book.title} removed from library!')

    def issue_book(self, book: Book, user: User):
        if book.isbn not in self.books:
            print('Book not found in catalogue')
            return False
        if user.mobile_no not in self.users:
            print('User not added to system, add user first!')
            return False
        library_book = self.books[book.isbn]
        if not library_book.get_is_borrowed():
            library_book.set_is_borrowed(True)
            library_book.set_borrowed_by(user.mobile_no)
            print(f'Book: ({library_book.title}) issued to User {user.name}')
            return True
        else:
            print(f'Book: ({library_book.title}) cant be issued')
            return False

    def return_book(self, book: Book):
        library_book = self.books[book.isbn]
        library_book.set_is_borrowed(False)
        library_book.set_borrowed_by(None)

    def list_books(self):
        if not self.books:
            print('No book available!')
            return
        print("List of Books available in catalogue")
        for book in self.books.values():
            print(book)

    def add_user(self, user: User):
        if user.mobile_no in self.users:
            print(f'User {user.name} with {user.mobile_no} already exist!')
            return
        self.users[user.mobile_no] = user
        print(f"User: {user.name} added to system!")

    def get_user_details(self, mobile_no: str) -> str:
        if mobile_no not in self.users:
            print("User details not found")
            return
        print(f'''User details:
                  Name: {self.users[mobile_no].name}
                  MNo : {self.users[mobile_no].mobile_no}
                  Email: {self.users[mobile_no].email}''')
        return self.users[mobile_no]
