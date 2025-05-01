class Car:
    def __init__(self, color: str, type: str, make: int, name: str = 'merc'):
        self.color = color
        self.type = type
        self.make = make
        self.__car_name = name
        print(f'''Your car details :
              color {self.color}
              type {self.type}
              make {self.make}''')

    def get_cost(self):
        print(f'''Current market price of the {self.make} car is INR 200k''')

    def __add__(self, other):  # default method override
        if isinstance(other, Car):
            print(f'''
                Combined details of both the cars are as follow
                {self.color} - {other.color}
                {self.type}  - {self.type}
                {self.make}  - {self.make}
                  ''')
            
    def __repr__(self):
        return f'Car  -> {self.color}, {self.type}, {self.make}'


merc: Car = Car('grey', 'sedan', 2024)
# audi: Car = Car('white', 'sedan', 2023)

# vehicle = merc + audi
merc.__car_name = 'Audi'
print(merc.__car_name)
