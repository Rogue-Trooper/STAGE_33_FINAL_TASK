from agency.model.entity.giver import Giver
from agency.model.entity.offer import Offer


def main():
    t1 = Offer()
    t2 = Offer()
    t3 = Offer()

    tours = [t1, t2, t3]

    tour = Giver.give_optimal_offer(tours)

    msg = tour()

    return msg


if __name__ == "__main__":
    main()
