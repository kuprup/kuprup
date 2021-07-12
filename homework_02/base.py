
class Vehicle():
    def __init__(self, weight=32,   fuel=1000, fuel_consumption=101):
        self.weight=weight
        self.fuel=fuel
        self.fuel_consumption=fuel_consumption
        self.started=True
    def __str__(self):
        return f'(weight={self.weight})(started=self.start)(fuel={self.fuel})(fuel_consumption={self.fuel_consumption} litters for 100 km)'
    def start (self, started):
        if self.fuel!=0:
            return self.started==True
        else:
            return self.started==False


car=Vehicle(32, 0, 101)
