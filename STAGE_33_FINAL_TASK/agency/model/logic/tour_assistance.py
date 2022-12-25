from agency.model.entity import *


class TourAssistance:
    @staticmethod
    def calculate_total_price(offer):
        if not isinstance(offer, Offer):
            return -1

        total = 0

        for tour in offer:
            if isinstance(tour, Tour):
                total = total + tour.price
        return total
