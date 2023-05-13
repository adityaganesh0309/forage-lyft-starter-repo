from .tire import Tire
from decimal import Decimal


class Octoprime(Tire):

    def __init__(self, tire_wear):
        super().__init__(tire_wear)

    def needs_service(self):
        decimal_tire_wear = [Decimal(str(value)) for value in self.tire_wear]

        # Calculate the sum using the decimal_tire_wear
        total = sum(decimal_tire_wear)
        return total >= 3.0
