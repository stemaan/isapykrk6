class Mammal:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        return f'Hi, this is {self.name}'

    def speak(self):
        return ''


class Human(Mammal):
    def speak(self):
        return f'Hi, my name is {self.name} I am human'


class Cat(Mammal):
    def __init__(self, name, has_long_hair=False):
        super().__init__(name)
        self.is_long_haired = has_long_hair

    def speak(self):
        return 'Meow!'

    def do_trick(self):
        return '<Rolls on the floor>'


class Persian(Cat):
    def __init__(self, name):
        super().__init__(name, has_long_hair=True)


if __name__ == '__main__':
    mammal = Mammal('Mammal')
    human = Human('Adam')
    kitty = Cat('kitty')
    jogis = Persian('Jogis')

    print(mammal.speak())
    print(human.speak())
    print(kitty.speak())

    print(jogis.speak())
    print(jogis.display_name())
    print(jogis.is_long_haired)

    # print(mammal.display_name())
    # print(human.name)
    # print(human.display_name())
    # print(human.speak())
    # print(kitty.speak())
    # print(kitty.do_trick())
    # print(kitty.is_long_haired)
    print(kitty.display_name())

    print(Cat.__mro__)
