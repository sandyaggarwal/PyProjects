from Library import Library
from Book import Book

# __name__ == __main__
library: Library = Library()

python_book: Book = Book('Building Python Microservices with FastAPI',
                         'Sherwin John C. Tragura', '49359437943')

library.add_book(python_book)
library.list_books()
