from Library import Library
from Book import Book
from User import User

# __name__ == __main__
library: Library = Library()

book1: Book = Book('Building Python Microservices with FastAPI',
                   'Sherwin John C. Tragura', '49359437943')
book2: Book = Book('Object-Oriented Python', 'Irv Kalb', '12874134792')
book3: Book = Book('Architecture Patterns with Python', 'Harry Percival',
                   '194943934')
book4: Book = Book('Mastering Python Design Patterns - Third Edition',
                   'Kamon Ayeva', '3482347594')

# add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.list_books()

user1: User = User('Rohit Raj', '9876543210', 'rohit.raj@abc.com')

library.add_user(user1)
library.get_user_details("9876543210")
library.issue_book(book1, user1)
print(book1)
library.return_book(book1)
print(book1)