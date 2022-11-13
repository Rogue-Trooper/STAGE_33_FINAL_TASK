# group: QA4822
# produced by: Siarhei Matsiash
# task about checking same elements of sequence

def check_same_digits(ls):
    answer = False
    for i in ls:
        if ls[i] == ls[i + 1]:
            answer = True
        return answer


def main():
    ls = [2, 2, 2, 2, 2, 2]
    # ls = [2, 2, 2, 1, 2, 2]

    answer = check_same_digits(ls)

    msg = f"Your sequence contains same digits" if answer else f"Your sequence does not contain same digits"

    print(msg)


main()
