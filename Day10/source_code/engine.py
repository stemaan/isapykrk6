__all__ = ['Engine']

print(__name__)


class Engine:
    def __init__(self, capacity: float, fuel: str):
        self.capacity = capacity
        self.fuel = fuel
        self.started = False

    def __str__(self):
        return f'Engine capacity {self.capacity}L, fuel {self.fuel}'

    def __repr__(self):
        return f'Engine({self.capacity}, {self.fuel})'

    def start(self):
        if not self.started:
            self.started = True

    def stop(self):
        if self.started:
            self.started = False


if __name__ == '__main__':
    hemi = Engine(6.2, 'PB')
    diesel = Engine(2.0, 'ON')

    print(hemi)
    print(diesel)
