from agency.model.entity import *

class Offer:
    def __init__(self):
        self._tours = []

    def add(self, tour):
        if isinstance(tour, Tour):
            self._tours.append(tour)

    def __bool__(self):
        return len(self._tours) != 0

    def __len__(self):
        return len(self._tours)

    def __getitem__(self, item):
        return self._tours[item]

    def __setitem__(self, key, value):
        self._tours[key] = value

    def __delitem__(self, key):
        del self._tours[key]

    def __str__(self):
        return f""
