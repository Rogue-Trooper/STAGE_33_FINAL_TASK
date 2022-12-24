TOURIST = 2


class Tour:

    def __init__(self, fare=0, hotel=0, insurance=0, price=0):
        self.fare = fare
        self.hotel = hotel
        self.insurance = insurance
        self.price = price

    @property
    def fare(self):
        return self.fare

    @fare.setter
    def fare(self, fare):
        if fare >= 0:
            self._fare = fare
        else:
            if not hasattr(self, "_fare"):
                self._fare = 0
            else:
                raise ValueError("Fare price was wrong")

    def set_fare(self, fare):
        if fare >= 0:
            self._fare = fare
        else:
            if not hasattr(self, "_fare"):
                self._fare = 0
            else:
                raise ValueError("Fare price was wrong")

    @fare.deleter
    def fare(self):
        del self._fare

    @property
    def hotel(self):
        return self.hotel

    @hotel.setter
    def hotel(self, hotel):
        if hotel >= 0:
            self._hotel = hotel
        else:
            if not hasattr(self, "_hotel"):
                self._hotel = 0
            else:
                raise ValueError("Hotel price was wrong")

    def set_hotel(self, hotel):
        if hotel >= 0:
            self._hotel = hotel
        else:
            if not hasattr(self, "_hotel"):
                self._hotel = 0
            else:
                raise ValueError("Hotel price was wrong")

    @hotel.deleter
    def hotel(self):
        del self._hotel

    @property
    def insurance(self):
        return self.insurance

    @insurance.setter
    def insurance(self, insurance):
        if insurance >= 0:
            self._insurance = insurance
        else:
            if not hasattr(self, "_insurance"):
                self._insurance = 0
            else:
                raise ValueError("Insurance price was wrong")

    def set_insurance(self, insurance):
        if insurance >= 0:
            self._insurance = insurance
        else:
            if not hasattr(self, "_insurance"):
                self._insurance = 0
            else:
                raise ValueError("Insurance price was wrong")

    @insurance.deleter
    def insurance(self):
        del self._insurance

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price >= 0:
            self._price = price
        else:
            if not hasattr(self, "_price"):
                self._price = 0
            else:
                raise ValueError("Tour price was wrong")

    def set_price(self, price):
        if price >= 0:
            self._price = price
        else:
            if not hasattr(self, "_price"):
                self._price = 0
            else:
                raise ValueError("Tour price was wrong")

    @price.deleter
    def price(self):
        del self._price

    def __str__(self):
        return f"fare = {self._fare}, " \
               f"hotel = {self._hotel}, " \
               f"insurance = {self._insurance}, " \
               f"price = {self._price}"
