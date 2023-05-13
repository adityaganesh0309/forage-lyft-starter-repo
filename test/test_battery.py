import unittest
from datetime import datetime

import sys
import os

# Add the parent directory of the 'car' package to the module search path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from battery.battery import Battery
from battery.helpers import battery_service_year
from battery.nubbin_battery import Nubbin
from battery.spindler_battery import Spindler

class TestBatteries(unittest.TestCase):

    def test_nubbin_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        nubbin = Nubbin(today, last_service_date)
        self.assertTrue(nubbin.needs_service())

    def test_nubbin_does_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        nubbin = Nubbin(today, last_service_date)
        self.assertFalse(nubbin.needs_service())

    def test_spindler_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        spindler = Spindler(today, last_service_date)
        self.assertTrue(spindler.needs_service())

    def test_spindler_does_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        spindler = Spindler(today, last_service_date)
        self.assertFalse(spindler.needs_service())


if __name__ == '__main__':
    unittest.main()