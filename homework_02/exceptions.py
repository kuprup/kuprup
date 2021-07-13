"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(BaseException):
     pass
class NotEnoughFuel(BaseException):
    pass
#h
class CargoOverload(BaseException):
    pass