import unittest
from datetime import datetime

import sys
import os

# Add the parent directory of the 'car' package to the module search path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from tire.tire import Tire
from tire.carrigan_tire import Carrigan
from tire.octoprime_tire import Octoprime

class TestTires(unittest.TestCase):

    def test_carrigan_needs_service(self):
        tire_wear = [0.9, 0.6, 1.0, 0.4]
        carrigan = Carrigan(tire_wear)
        self.assertTrue(carrigan.needs_service())

    def test_carrigan_does_not_need_service(self):
        tire_wear = [0.7, 0.6, 0.5, 0.4]
        carrigan = Carrigan(tire_wear)
        self.assertFalse(carrigan.needs_service())

    def test_octoprime_needs_service(self):
        tire_wear = [0.7, 0.7, 0.7, 0.9]
        octoprime = Octoprime(tire_wear)
        self.assertTrue(octoprime.needs_service())

    def test_octoprime_does_not_need_service(self):
        tire_wear = [0.7, 0.7, 0.7, 0.8]
        octoprime = Octoprime(tire_wear)
        self.assertFalse(octoprime.needs_service())


if __name__ == '__main__':
    unittest.main()