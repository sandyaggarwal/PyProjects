class Book:

    def __init__(self, title, author, isbn):
        self.title: str = title
        self.author: str = author
        self.isbn: str = isbn
        self.__is_borrowed: bool = False
        self.__borrowed_by: str = None

    def set_is_borrowed(self, is_borrowed: bool):
        self.__is_borrowed = is_borrowed

    def get_is_borrowed(self) -> bool:
        return self.__is_borrowed

    def set_borrowed_by(self, name: str):
        self.__borrowed_by = name

    def get_borrowed_by(self, isbn: str) -> str:
        return self.__borrowed_by

    def __str__(self):
        return (f'Book(TItle:{self.title}, Author:{self.author},'
                f'ISBN:{self.isbn},'
                f'Borrowed: {"Yes" if self.__is_borrowed else "No"}'
                f'Borrowed By:'
                f'{self.get_borrowed_by if self.__is_borrowed else None})')
