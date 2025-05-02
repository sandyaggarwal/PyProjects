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
