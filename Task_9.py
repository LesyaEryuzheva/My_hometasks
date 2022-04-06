from dataclasses import dataclass

@dataclass
class Footwear:
    season: str
    size: int
    material: str

    @staticmethod
    def get_description():
        print('There is a large selection of shoes here!')

print(Footwear.get_description())

sneakers = Footwear('spring', 38, 'leather')
print(sneakers)

@dataclass
class Menu:
    appetizers: str
    desserts: str
    salads: str
    drinks: str

food = Menu('nachos', 'ice-cream', 'garden fresh salad', 'coffee')

print(food)

@dataclass
class Puzzle:
    amount_of_elements: int
    themes: str
    recommended_age: str

plaything = Puzzle(400, 'dinosaur', 'garden fresh salad')

print(plaything)


@dataclass
class Person:
    age: int
    gender: str

    @staticmethod
    def retirement_age(age, gender):
        if age >= 58 and gender == 'women':
            return True
        elif age >= 63 and gender == 'man':
            return True
        else:
            return False

print(Person.retirement_age(63, 'man'))

@dataclass
class Product:
    name: str
    price: int

    @classmethod
    def get_a_discount(cls, name, new_price):
        return cls(name, new_price - (new_price * 0.3))

bakery = Product('bread', 5)
cheese = Product.get_a_discount('brie', 20)

print(bakery.price)
print(cheese.price)
