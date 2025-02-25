from abc import ABC
from engine.engine import Engine

class CapuletEngine(Engine, ABC):
    def __init__(self, current_mileage, last_service_mileage):
        super().__init__(current_mileage, last_service_mileage)

    def needs_service(self):
        return (self.current_mileage - self.last_service_mileage) > 3000
