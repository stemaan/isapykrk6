from source_code.engine import Engine


class Car:
    def __init__(self, manufacturer, model, color='white', engine=None):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.engine = engine

    def __str__(self):
        return f'Car {self.manufacturer} {self.model} engine: {self.engine} color: {self.color}'

    def start_car(self):
        self.engine.start()

    def stop_car(self):
        self.engine.stop()


if __name__ == '__main__':
    cheeroke = Car('Jeep', 'Cheeroke', 'Red')

    print(cheeroke)

    hemi = Engine(6.2, 'PB')
    cheeroke.engine = hemi
    print(cheeroke)

    matiz_engine = Engine(0.8, 'PB')
    matiz = Car('Daewoo', 'Matiz', 'Gold', matiz_engine)

    print(matiz)
