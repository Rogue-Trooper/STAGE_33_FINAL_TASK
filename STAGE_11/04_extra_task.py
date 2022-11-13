# group: QA4822
# produced by: Siarhei Matsiash
# task about marks and finding %

import random

BEGINNING_OF_SEQUENCE = 0
END_OF_SEQUENCE = 5
ONE = 1
ONE_HUNDRED = 100


def get_sum_mark_five(numbers):
    count = 0

    for element in numbers:
        if element == 5:
            count = count + 1

    return count


def get_sum_mark_four(numbers):
    count = 0

    for element in numbers:
        if element == 4:
            count = count + 1

    return count


def get_sum_mark_three(numbers):
    count = 0

    for element in numbers:
        if element == 3:
            count = count + 1

    return count


def get_sum_mark_two(numbers):
    count = 0

    for element in numbers:
        if element == 2:
            count = count + 1

    return count


def get_sum_mark_one(numbers):
    count = 0

    for element in numbers:
        if element == 1:
            count = count + 1

    return count


def get_sum_mark_zero(numbers):
    count = 0

    for element in numbers:
        if element == 0:
            count = count + 1

    return count


def find_percent_mark_five(numbers, five):
    percent_mark_five = (five / len(numbers)) * ONE_HUNDRED
    return percent_mark_five


def find_percent_mark_four(numbers, four):
    percent_mark_four = (four / len(numbers)) * ONE_HUNDRED
    return percent_mark_four


def find_percent_mark_three(numbers, three):
    percent_mark_three = (three / len(numbers)) * ONE_HUNDRED
    return percent_mark_three


def find_percent_mark_two(numbers, two):
    percent_mark_two = (two / len(numbers)) * ONE_HUNDRED
    return percent_mark_two


def find_percent_mark_one(numbers, one):
    percent_mark_one = (one / len(numbers)) * ONE_HUNDRED
    return percent_mark_one


def find_percent_mark_zero(numbers, zero):
    percent_mark_zero = (zero / len(numbers)) * ONE_HUNDRED
    return percent_mark_zero


def main():
    number_of_digit = int(input("Input number of digits in your sequence: "))

    numbers = []
    while number_of_digit > 0:
        number_of_digit = number_of_digit - 1
        digit = random.randrange(BEGINNING_OF_SEQUENCE, END_OF_SEQUENCE + 1)
        numbers.append(digit)

    five = get_sum_mark_five(numbers)
    four = get_sum_mark_four(numbers)
    three = get_sum_mark_three(numbers)
    two = get_sum_mark_two(numbers)
    one = get_sum_mark_one(numbers)
    zero = get_sum_mark_zero(numbers)

    percent_mark_five = find_percent_mark_five(numbers, five)
    percent_mark_four = find_percent_mark_four(numbers, four)
    percent_mark_three = find_percent_mark_three(numbers, three)
    percent_mark_two = find_percent_mark_two(numbers, two)
    percent_mark_one = find_percent_mark_one(numbers, one)
    percent_mark_zero = find_percent_mark_zero(numbers, zero)

    msg_five = f"Sequence contains {five} digits five ({percent_mark_five}%)"
    msg_four = f"Sequence contains {four} digits four ({percent_mark_four}%)"
    msg_three = f"Sequence contains {three} digits three ({percent_mark_three}%)"
    msg_two = f"Sequence contains {two} digits two ({percent_mark_two}%)"
    msg_one = f"Sequence contains {one} digits one ({percent_mark_one}%)"
    msg_zero = f"Sequence contains {zero} digits zero ({percent_mark_zero}%)"

    print(numbers)
    print(msg_five)
    print(msg_four)
    print(msg_three)
    print(msg_two)
    print(msg_one)
    print(msg_zero)


main()
