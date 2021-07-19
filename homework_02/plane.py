"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight=32, fuel=1000, fuel_consumption=10, max_cargo=12, cargo=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False
        self.cargo = cargo
        self.max_cargo = max_cargo

    def __str__(self):
        return f'{self.weight}fuel={self.fuel}fuelconsumption={self.fuel_consumption}cargo={self.cargo}max_cargo={self.max_cargo}'

    def load_cargo(self, additiona_lcargo):
        if (self.cargo + additional_cargo) > self.max_cargo:
            raise CargoOverload('You have the overload')
        else:
            self.cargo = +additional_cargo

    def remove_all_cargo(self):
        removed_cargo=self.cargo
        print(removed_cargo)
        self.cargo=0
        return removed_cargo
#print(Plane(5).load_cargo(1))
#Plane(4).remove_all_cargo()
#print(Plane(10).remove_all_cargo())