from Book import Book


class Library:
    def __init__(self):
        self.books: list[Book] = []
    
    def add_book(self, book: Book):
        self.Books.append(book)
            
    def remove_book(self, book: Book):
        self.books.pop(book)
    
    def issue_book(self, book: Book):
        book.set_is_borrowed(True)
        
    def return_book(self, book: Book):
        book.set_is_borrowed(False)
        
    def list_books(self) -> list[Book]:
        if not self.books:
            print('No book available!')
        for book in self.books:
            print(book)
        return self.books # noqa