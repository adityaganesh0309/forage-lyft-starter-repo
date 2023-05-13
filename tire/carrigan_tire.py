from .tire import Tire

class Carrigan(Tire):

    def __init__(self, tire_wear):
        super().__init__(tire_wear)

    def needs_service(self):
        for val in self.tire_wear:
            if val >= 0.9: return True
        return False