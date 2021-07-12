"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine
class Car(Vehicle):
    def __init__(self, weight=32,   fuel=1000, fuel_consumption=10, engine='none'):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = True
        self.engine=engine
    def __str__(self):
        return f'(weight={self.weight})(Move={self.__start__(self.fuel)})(fuel={self.fuel})(fuel_consumption={self.fuel_consumption} litters for 100 km)(engine={self.__set_engine__()}'
    def __set_engine__(self):
        a=int(input('set volume'))
        b=int(input('set pistons'))
        return Engine(volume=a, pistons=b)

print(Car())

