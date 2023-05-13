from abc import ABC, abstractmethod
from serviceable import Serviceable
import datetime

class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service() or self.tire.needs_service()
