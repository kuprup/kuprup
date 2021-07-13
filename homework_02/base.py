from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle():
    def __init__(self, weight=32, fuel=1000, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = True

    def __str__(self):
        return f'(weight={self.weight})(Move={self.start(self.fuel)})(fuel={self.fuel})(fuel_consumption={self.fuel_consumption} litters for 100 km)'

    def start(self, fuel):
        if not self.started:
            if fuel > 0:
               self.started=True
            else:
               raise LowFuelError('You do not have enough fuel')

    def move(self, distance):
        how_many_can_move = self.fuel*self.fuel_consumption
        ostatok = self.fuel - distance*self.fuel_consumption
        if how_many_can_move >= distance:
            print('You have enough fuel for this distance and you also have ' + str(ostatok) + ' litres')
        else:
            raise NotEnoughFuel('You do not have enough fuel')

# car=Vehicle(32, 1010, 10)
# print(car)

# car.__move__(91000, car.fuel_consumption)
