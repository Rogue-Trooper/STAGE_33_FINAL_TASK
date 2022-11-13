# group: QA4822
# produced by: Siarhei Matsiash
# task about looking for min, max, middle arithmetical sum, counts the number of positive, negative and zero
# EXCHANGE DOES NOT WORK(

import random


def get_max(numbers):
    max = numbers[0]

    for element in numbers:
        if element > max:
            max = element

    return max


def get_min(numbers):
    min = numbers[0]

    for element in numbers:
        if element < min:
            min = element

    return min


def calc_arithmetical_avg(numbers):
    s = 0

    for num in numbers:
        s = s + num

    return s / len(numbers)


def calc_positive_digits(numbers):
    positive = 0

    for num in numbers:
        if num > 0:
            positive = positive + 1

    return positive


def calc_negative_digits(numbers):
    negative = 0

    for num in numbers:
        if num < 0:
            negative = negative + 1

    return negative


def calc_zero_digits(numbers):
    zero = 0

    for num in numbers:
        if num == 0:
            zero = zero + 1

    return zero


def find_min_index(numbers):
    min_index = numbers[0]
    for index in range(numbers[len(numbers) - 1]):
        if numbers[0] > numbers[index + 1]:
            min_index = numbers[index + 1]

        return min_index


def find_max_index(numbers):
    max_index = numbers[0]
    for index in range(numbers[len(numbers) - 1]):
        if numbers[index] < numbers[index + 1]:
            max_index = numbers[index + 1]

        return max_index


def exchange_extremes(numbers):
    min_index = 0
    for index in range(1, len(numbers)):
        if numbers[index] < numbers[min_index]:
            min_index = index

            max_j = 0
            for j in range(1, len(numbers)):
                if numbers[j] > numbers[max_j]:
                    max_j = j

            t = numbers[min_index]
            numbers[min_index] = numbers[max_j]
            numbers[max_j] = t

    return numbers


def main():
    beginning_of_sequence = int(input("Input beginning of your sequence: "))
    end_of_sequence = int(input("Input end of your sequence: "))
    number_of_digit = int(input("Input number of digits in your sequence: "))

    numbers = []
    while number_of_digit > 0:
        number_of_digit = number_of_digit - 1
        digit = random.randrange(beginning_of_sequence, end_of_sequence + 1)
        numbers.append(digit)

    max_x = get_max(numbers)
    min_n = get_min(numbers)
    medium_arithmetical = calc_arithmetical_avg(numbers)
    positive_digit = calc_positive_digits(numbers)
    negative_digit = calc_negative_digits(numbers)
    zero_digit = calc_zero_digits(numbers)
    exchange = exchange_extremes(numbers)

    msg_x = f"max digit is: {max_x}"
    msg_n = f"min digit is: {min_n}"
    msg_arithmetical = f"medium arithmetical is {round(medium_arithmetical, 2)}"
    msg_positive = f"Your sequence has {positive_digit} positive digits"
    msg_negative = f"Your sequence has {negative_digit} negative digits"
    msg_zero = f"Your sequence has {zero_digit} zero digits"
    msg_exchange = f"{exchange}"

    print(numbers)
    print(msg_x)
    print(msg_n)
    print(msg_arithmetical)
    print(msg_positive)
    print(msg_negative)
    print(msg_zero)
    print(msg_exchange)


main()
