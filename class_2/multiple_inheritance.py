class Movable(object):
    pass

class OpenDooralbe(object):
    pass

class FiilFuelTankable(object):
    pass

class Car(Movable, OpenDooralbe, FiilFuelTankable):
    pass


class AirVehicle(object):
    def move(self):
        print("AirVehicle on the move!")


class GroundVehicle(object):
    def move(self):
        print("GroundVehicle on the move!")


class Airplane(GroundVehicle, AirVehicle):
    pass


a = Airplane()
a.move()