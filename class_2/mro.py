class Vehicle(object):
    def __init__(self):
        self.name = 'General Vehicle'

    def move(self):
        print('{} moving'.format(self.name))


class Car(Vehicle):
    COLOR = 'Red'

    def __init__(self, name):
        self.name = name


c1 = Car('Ford')
# c1.COLOR = 'BLUE'
c2 = Car('Chevy')

print(c1.COLOR)
print(c2.COLOR)