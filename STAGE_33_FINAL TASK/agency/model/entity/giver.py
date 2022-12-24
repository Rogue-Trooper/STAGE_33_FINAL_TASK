from agency.model.entity.tour import TOURIST

class Giver:
    @staticmethod
    def give_optimal_offer(tours):
        if not isinstance(tours, list):
            return

        itour = 0

        for index in range(1, len(tours)):
            current = tours[index].tour / TOURIST
            max = tours[itour].tour / TOURIST

            if current > max:
                itour = index

        return tours[itour]
