class Worker:
    num_of_workers = 0
    yearly_rise = 0.1

    def __init__(self, name):
        self.name = name
        self.salary = 4500
        Worker.num_of_workers += 1

    def give_rise(self):
        self.salary += self.salary * Worker.yearly_rise

    @classmethod
    def set_yearly_rise(cls, yearly_rise):
        if yearly_rise >= 0.1:
            cls.yearly_rise = 0.1
        else:
            cls.yearly_rise = yearly_rise


if __name__ == '__main__':
    worker = Worker('Jan kowalski')
    worker2 = Worker('Adam Nowak')
    print(Worker.num_of_workers)
    print(worker2.num_of_workers)

    worker2.give_rise()
    print(worker.salary)
    print(worker2.salary)

    Worker.set_yearly_rise(0.05)
    worker.give_rise()
    print(worker.salary)