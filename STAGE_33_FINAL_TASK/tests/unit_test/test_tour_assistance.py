import unittest

from agency.model.entity import *
from agency.model.logic import *


class TestTourAssistance(unittest.TestCase):

    def test_calculate_total_price_basic(self):
        offer = Offer()
        offer.add(Tour(30))
        offer.add(Tour(15))
        offer.add(Tour(55))
        expected = 100

        actual = TourAssistance.calculate_total_price(offer)

        self.assertEqual(expected, actual)

    def test_calculate_total_price_with_incorrect_data(self):
        expected = -1
        actual = TourAssistance.calculate_total_price(7)
        self.assertEqual(expected, actual)

    def test_calculate_total_price_with_empty_offer(self):
        expected = 0
        actual = TourAssistance.calculate_total_price(Offer())
        self.assertEqual(expected, actual)

    def test_calculate_total_price_with_only_one_offer(self):
        offer = Offer()
        tour = Tour(5)
        offer.add(tour)
        expected = tour.price
        actual = TourAssistance.calculate_total_price(offer)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
