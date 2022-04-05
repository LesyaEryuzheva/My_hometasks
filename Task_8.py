class Toy():
    def __init__(self, toy_type, age, gender):
        self.toy_type = toy_type
        self.age_restrictions = age
        self.gender_of_the_child = gender

    def get_descriptive_name (self):
        description = f"Если у вас {self.gender_of_the_child} в возрасте {self.age_restrictions} лет ему понравится {self.toy_type}."
        return description


lego = Toy('констуктор', 6, 'мальчик')
print(lego.get_descriptive_name())


class MusicalToy(Toy):
    def __init__(self, toy_type, age, gender, battery):
        super().__init__(toy_type, age, gender)
        self.battery = battery
        if age <= 3:
           print('Нежелательно использовать детям до 3 лет')
        else:
            print('Вашему ребенку можно предложить музыкальную игрушку.')

    def __str__(self) -> str:
        description = f"{self.toy_type} является {self.gender_of_the_child} и понравится любому ребенку " \
                      f"своими веселыми мелодиями."
        return description

    def get_descriptive_name(self):
        description = f"Музыкальная игрушка {self.toy_type} работает от батареек типа {self.battery}."
        return description


synthesizer = MusicalToy('синтезатор', 4, 'универсальный', 'ААА')
print(synthesizer)
print(synthesizer.get_descriptive_name())


class SoftToy (Toy):
    def __init__(self, toy_type, age, gender, filler):
        super().__init__(toy_type, age, gender)
        self.filler = filler

    def __str__(self) -> str:
        description = f"Если у вас {self.gender_of_the_child} в возрасте {self.age_restrictions} лет " \
                      f"обратите внимание на игрушку {self.toy_type}, он очень мягкий ведь внутри него {self.filler}."

        return description


Bear = SoftToy('мишка', 2, 'девочка', 'натуральный пух')
print(Bear)