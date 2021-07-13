"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight=32, fuel=1000, fuel_consumption=10, cargo=1000,  max_cargo=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = True
        self.cargo=cargo
        self.max_cargo=max_cargo
    def