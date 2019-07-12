class Animal:
    def __init__(self, name):
        print('__init__ w klasie Animal')
        self.name = name

    def speak(self):
        print(f'Hej jestem {self.name}')


class Horse(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('__init__ w klasie Horse')

    def speak(self):
        print(f'Hej jestem kon')


class Donkey(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('__init__ w klasie Donkey')

    def speak(self):
        print(f'Hej jestem osiol')


class Mule(Horse, Donkey):
    def speak(self):
        print(f'Hej jestem {self.name}')
        super().speak()


if __name__ == '__main__':
    animal = Animal('animal')
    print('*'*80)
    horse = Horse('kon')
    print('*'*80)
    donkey = Donkey('osiol')
    print('*'*80)
    mule = Mule('mul')
    mule.speak()