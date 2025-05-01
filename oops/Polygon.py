class Polynomial:
    __width = None
    __height = None

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


class Rectangle(Polynomial):
    def __init__(self):
        super().__init__()

    def get_area(self):
        area = self.get_width() * self.get_height()
        print(f'area of the Rectangle is {area}')
        return area
    

class Traingle(Polynomial):
    def __init__(self):
        super().__init__()

    def get_area(self):
        area = (self.get_height() * self.get_width())/2
        print(f'area of the triangle is {area}')
        return area
        

tria: Traingle = Traingle()
rect: Rectangle = Rectangle()
tria.set_height(20)
tria.set_width(30)

tria.get_area()

rect.set_height(10)
rect.set_width(90)
rect.get_area()