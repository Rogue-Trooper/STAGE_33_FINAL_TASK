# group: QA4822
# produced by: Siarhei Matsiash
# task about looking for sum of even/uneven digits in sequence

import random


def look_for_even(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0 and numbers[i] != 0:
            count = count + 1
    return count


def look_for_uneven(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0 and numbers[i] != 0:
            count = count + 1
    return count


def main():
    beginning_of_sequence = int(input("Input beginning of your sequence: "))
    end_of_sequence = int(input("Input end of your sequence: "))
    number_of_digit = int(input("Input number of digits in your sequence: "))

    numbers = []
    while number_of_digit > 0:
        number_of_digit = number_of_digit - 1
        digit = random.randrange(beginning_of_sequence, end_of_sequence + 1)
        numbers.append(digit)

    even = look_for_even(numbers)
    uneven = look_for_uneven(numbers)

    msg_even = f"Your sequence has {even} even digits"
    msg_uneven = f"Your sequence has {uneven} uneven digits"

    print(numbers)
    print(msg_even)
    print(msg_uneven)


main()
