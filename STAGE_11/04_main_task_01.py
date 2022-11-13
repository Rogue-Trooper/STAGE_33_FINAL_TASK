# group: QA4822
# produced by: Siarhei Matsiash
# task about checking increasing or decreasing elements of sequence

def check_increasing_sequence(ls):
    for i in range(len(ls) - 1):
        if ls[i] < ls[i + 1]:
            return True


def main():
    ls = [15, 13, 8, 7, 2, 1]
    #ls = [1, 2, 8, 9, 15, 22]

    check_increasing_sequence(ls)

    msg = f"Your sequence is increasing" if check_increasing_sequence(ls) else f"Your sequence is decreasing"

    print(msg)


main()
