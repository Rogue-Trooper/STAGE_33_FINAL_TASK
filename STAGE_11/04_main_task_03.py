# group: QA4822
# produced by: Siarhei Matsiash
# task about checking  if this sequence is palindrome
# IT DOES NOT WORK WITH SEQUENCE LIKE THIS ls = [1, 2, 1, 1, 2, 1]

def check_palindrome(ls):
    answer = False
    for i in ls:
        if ls[i] == ls[len(ls)-1-i]:
            answer = True
        return answer


def main():
    #ls = [1, 2, 1, 1, 2, 1]

    ls = [1, 2, 5, 7, 3, 0]

    answer = check_palindrome(ls)

    msg = f"Your sequence is palindrome" if answer else f"Your sequence is not palindrome"

    print(msg)


main()
