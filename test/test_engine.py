import unittest

import sys
import os

# Add the parent directory of the 'car' package to the module search path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from engine.engine import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestEngines(unittest.TestCase):

    def test_capulet_needs_service(self):
        current_mileage = 7000
        last_service_mileage = 2000 
        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())

    def test_capulet_does_not_need_service(self):
        current_mileage = 7000
        last_service_mileage = 6000 
        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet.needs_service())

    def test_sternman_needs_service(self):
        light = True
        sternman = SternmanEngine(light)
        self.assertTrue(sternman.needs_service())

    def test_sternman_does_not_need_service(self):
        light = False
        sternman = SternmanEngine(light)
        self.assertFalse(sternman.needs_service())

    def test_willoughby_needs_service(self):
        current_mileage = 15000
        last_service_mileage = 6000 
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby.needs_service())

    def test_willoughby_does_not_need_service(self):
        current_mileage = 7000
        last_service_mileage = 6000 
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby.needs_service())


if __name__ == '__main__':
    unittest.main()