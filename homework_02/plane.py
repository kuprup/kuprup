"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption,  max_cargo, cargo=0):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.max_cargo=max_cargo
        self.cargo=cargo



    def __str__(self):
        return f'{self.weight}fuel={self.fuel}fuelconsumption={self.fuel_consumption}cargo={self.cargo}max_cargo={self.max_cargo}'

    def load_cargo(self, additional_cargo):
        if (self.cargo + additional_cargo) > self.max_cargo:
            raise CargoOverload('You have the overload')
        else:
            new_cargo=self.cargo+additional_cargo
            self.cargo = new_cargo

    def remove_all_cargo(self):
        removed_cargo=self.cargo
        print(removed_cargo)
        self.cargo=0
        return removed_cargo
