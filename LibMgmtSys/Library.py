from Book import Book


class Library:
    def __init__(self):
        self.Books: list[Book] = []
    
    def add_book(self, book: Book):
        self.Books.append(book)
            
    def remove_book(self, book: Book):
        self.Books.pop(book)
    
    def issue_book(self, book: Book):
        book.set_is_borrowed(True)
        
    def return_book(self, book: Book):
        book.set_is_borrowed(False)
        
        