from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle():
    def __init__(self, weight=32, fuel=1000, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def __str__(self):
        return f'(weight={self.weight})(Move={self.start(self.fuel)})(fuel={self.fuel})(fuel_consumption={self.fuel_consumption} litters for 100 km)'

    def start(self):
        if not self.started:
            if self.fuel > 0:
               self.started=True
            else:
               raise LowFuelError('You do not have enough fuel')

    def move(self, distance):
        if self.fuel<(distance*self.fuel_consumption):
            raise NotEnoughFuel('You do not have enough fuel')
        else:
            self.fuel-=(self.fuel_consumption*distance)

