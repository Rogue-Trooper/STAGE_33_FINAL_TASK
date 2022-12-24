import unittest
from agency.model.entity import *


class TestTour(unittest.TestCase):
    def test_setter_positive(self):
        tour = Tour()
        tour.price = 10

        expected = 10
        actual = tour.price

        self.assertEqual(expected, actual)

    def test_setter_without_price(self):
        tour = Tour()

        expected = 0
        actual = tour.price

        self.assertEqual(expected, actual)

    def test_setter_negative(self):
        tour = Tour()

        self.assertEqual(ValueError, tour.set_price, 10)


if __name__ == "__main__":
    unittest.main()
