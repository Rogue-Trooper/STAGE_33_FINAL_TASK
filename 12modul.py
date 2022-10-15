def search_element(ls, target):
    a = 0
    b = len(ls) - 1

    while a <= b:
        middle = (a + b) // 2
        if ls[middle] == target:
            return True
        elif ls[middle] > target:
            b = middle - 1
        else:
            a = middle + 1

    return False


def main():
    ls = [5, 8, 12, 27, 29, 35, 39, 59, 62, 67, 77, 79, 89]
    target = int(input("Input looking for digit: "))

    result = search_element(ls, target)

    msg = (f"Looking for digit {target} presents in {ls} list" if result == True
           else f"Looking for digit {target} does not present in list")

    print(msg)


main()
