class Book:
    def __init__(self, title, author, isbn):
        self.title: str = title
        self.author: str = author
        self.isbn: str = isbn
        self.__is_borrowed: bool = False
        
    def set_is_borrowed(self, is_borrowed: bool):
        self.__is_borrowed = is_borrowed
    
    def get_is_borrowed(self) -> bool:
        return self.__is_borrowed

       
# famous_five: Book = Book('Famous Five', 'Unknown', '9234879237')
# famous_five.set_is_borrowed(True)
# print(f'Book {famous_five.title} status {famous_five.get_is_borrowed()}')   
