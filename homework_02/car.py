"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(self, weight=32, fuel=1000, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False
        self.engine = engine

    def __str__(self):
        return f'(weight={self.weight})(Move={self.start(self.fuel)})(fuel={self.fuel})(fuel_consumption={self.fuel_consumption} litters for 100 km)(engine={self.engine})'

    def set_engine(self, engine):
        engine=Engine
        self.engine = engine


