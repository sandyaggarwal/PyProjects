class Car:
    def __init__(self, color: str, type: str, make: int):
        self.color = color
        self.type = type
        self.make = make
        print(f'''Your car details :
              color {self.color}
              type {self.type}
              make {self.make}''')

    def get_cost(self):
        print(f'''Current market price of the {self.make} car is INR 200k''')

    def __add__(self, other):
        print('Details of both the cars are cant be combined')


merc: Car = Car('grey', 'sedan', 2024)
audi: Car = Car('white', 'sedan', 2023)
merc.get_cost()

vehicle = merc + audi
