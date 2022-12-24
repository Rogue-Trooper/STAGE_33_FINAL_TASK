# определение кол-ва дней необходимых для достижения дистанции h при подъёме на а м/12 час и спускании на b м/12 час при h>b and a>b
# def get_time(h, a, b):
#     day = 0
#
#     while h >= 0:
#         h = h - a
#         day = day + 1
#
#         if h <= 0:
#             return day
#         else:
#             h = h + b
#
#
# def main():
#     h = int(input("Input h: "))
#     a = int(input("Input a: "))
#     b = int(input("Input b: "))
#
#     day = get_time(h, a, b)
#
#     msg = (f"if your snail moves up with {a} m/12 hour and move down with {b} m/12 hours "
#            f"it will pass distance in {h} m in {day} days")
#
#     print(msg)
#
#
# main()

# TASK 1 поиск у заданого времени суммы в часах минутах и секундах
# SEK_IN_MIN = 60
# MIN_IN_HOUR = 60
# HOUR_IN_DAY = 24
#
#
# def find_time(a, b, c):
#     return a, a * MIN_IN_HOUR + b, a * MIN_IN_HOUR * SEK_IN_MIN + b * SEK_IN_MIN + c
#
#
# x, y, z = int(input("input your hour: ")), int(input("input your minute: ")), int(input("input your second: "))
# hour, minute, sec = find_time(x, y, z)
#
# msg = f"Your time has {hour} hours or {minute} minutes or {sec} seconds"
# print(msg)

# TASK 2 поиск суммы цифр заданого числа
# def sum_finder(a):
#     su = 0
#     while a // 10 != 0:
#         su = su + a % 10
#         a = a // 10
#     return su + a % 10
#
#
# number = int(input("input your number :"))
# su = sum_finder(number)
# msg = f"sum digits of your number is {su}"
# print(msg)

# TASK 3 выполнить реверс числа
# def revers_finder(a):
#     number = 0
#     while a > 0:
#         digit = a % 10
#         a = a // 10
#         number = number * 10
#         number = number + digit
#     return number
#
#
# def main():
#     a = int(input("input your 4 digits :"))
#     revers = revers_finder(a)
#     msg = f"revers of your number {a} is {revers}"
#     print(msg)
#
#
# main()

# TASK 4 Определение столетия
# import math
#
#
# def finder_century(year):
#     cent = math.ceil(year / 100)
#     return cent
#
#
# def main():
#     year = int(input("input interesting you year :"))
#     cent = finder_century(year)
#     msg = f"interesting you year is in {cent} century"
#     print(msg)
#
#
# main()

# while - пример цикла
# def hello(count):
#     while count > 0:
#         print("hello")
#         count = count - 1
#
#
# def main():
#     count = 5
#     hello(count)
#
#
# main()

# def hello(count):
#     msg = ""
#     while count > 0:
#         msg = msg + "Hello!!!"'\n'
#         count = count - 1
#     return msg
#
#
# def main():
#     count = 3
#     print(hello(count))
#
#
# main()

# сумма чисел в цикле while
# def sum_num(x):
#     s_n = 0
#     while x > 0:
#         s_n = s_n + x % 10
#         x = x // 10
#     return s_n
#
#
# def main():
#     a = int(input("input your number :"))
#     s_n = sum_num(a)
#     msg = f"sum digit's of your number {a} is {s_n}"
#     print(msg)
#
#
# main()

# максимальное число
# def get_max_digit(number):
#     number *= -1 if number < 0 else 1
#
#     max_digit = 0
#
#     while number > 0:
#         digit = number % 10
#
#         if digit == 9:
#             max_digit = 9
#             break
#
#         if digit > max_digit:
#             max_digit = digit
#         number = number // 10
#
#     return max_digit
#
#
# def main():
#     number = int(input("input your number :"))
#     max_digit = get_max_digit(number)
#     msg = f"max digit in your number is {max_digit}"
#     print(msg)
#
#
# main()

# n!
# def fac(number):
#     if number < 0:
#         return -1
#     else:
#         f = 1
#         for item in range(2, number + 1):
#             f = f * item
#         return f
#
#
# def main():
#     number = int(input("input :"))
#     result = fac(number)
#     if result != -1:
#         msg = f"{number}! is {result}"
#     else:
#         msg = f"invalid number"
#     print(msg)
#
#
# main()

# вывод номер элемента (индекса) и содержимое элемента (индекса)
# numbers = [1, 57, 3, 83, 5, 67, 72, 62]
#
# for index in range(len(numbers)):
#     print(f"{index} - {numbers[index]}")

# ввод оценок и определение среднего арифмитического
# def calc_avg_marks(marks):
#     s = 0
#
#     for element in marks:
#         s = s + element
#
#     return (s) / len(marks)
#
#
# def main():
#     marks = []
#
#     mark = 0
#
#     print("input marks.\nFor exit input -1\n")
#
#     while mark != -1:
#         mark = int(input("input :"))
#         if mark != -1:
#             marks.append(mark)
#
#     avg = calc_avg_marks(marks)
#
#     msg = f"middle mark of students is {round(avg, 2)}"
#
#     print(msg)
#
#
# main()

# поиск максимального и минимального содержимого среди элементов контейнера с указанием индекса элемента
# def get_max(numbers):
#     max = numbers[0]
#
#     for element in numbers:
#         if element > max:
#             max = element
#
#     return max
#
#
# def get_max_value_index(numbers):
#     max = numbers[0]
#
#     for element in range(len(numbers)):
#         if element > max:
#             max = element
#
#     return max
#
#
# def get_min(numbers):
#     min = numbers[0]
#
#     for element in numbers:
#         if element < min:
#             min = element
#
#     return min
#
#
# def get_min_value_index(numbers):
#     min = numbers[0]
#
#     for element in range(0, len(numbers)):
#         if element < min:
#             min = element
#
#     return min
#
#
# def calc_arithmetical_avg(numbers):
#     s = 0
#
#     for num in numbers:
#         s = s + num
#
#     return s / len(numbers)
#
#
# def calc_geometrical_avg(numbers):
#     p = 1
#
#     for num in numbers:
#         p = p * num
#
#     return p**(1/len(numbers))
#
#
# def main():
#     numbers = [1, 57, 3, 83, 5, 67, 83, 1]
#
#     max_x = get_max(numbers)
#     max_x_i = get_max_value_index(numbers)
#     min_n = get_min(numbers)
#     min_n_i = get_min_value_index(numbers)
#     medium_arithmetical = calc_arithmetical_avg(numbers)
#     geometrical_avg = calc_geometrical_avg(numbers)
#
#     msg_x = f"index with max number is {max_x_i} - {max_x}"
#     msg_n = f"index with min number is {min_n_i} - {min_n}"
#     msg_arithmetical = f"medium arithmetical is {round(medium_arithmetical, 2)}"
#     msg_geometrical = f"geometrical avg is {round(geometrical_avg, 2)}"
#
#     print(msg_x)
#     print(msg_n)
#     print(msg_arithmetical)
#     print(msg_geometrical)

#TABLE OF PYTHAGORAS
# def get_pythagoras_table(number):
#     table = ""
#
#     for j in range(1, number + 1):
#         for i in range(1, number + 1):
#             table = table + f"{i * j}\t"
#
#         table = table + "\n"
#
#     return table
#
#
# def main():
#     number = int(input("input your number :"))
#     table = get_pythagoras_table(number)
#     print(table)
#
#
# main()

# поиск нахождения элемента в списке
# def find_value(ls, value):
#     answer = False
#     for item in ls:
#         if item == value:
#             answer = True
#             break
#
#     return answer

# поиск нахождения элемента в списке
# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# value = 4
#
# print(value in ls)

# поиск нахождения элемента в списке
# def find_value(ls, value):
#     for item in ls:
#         if item == value:
#             return True
#
#     return False
#
#
# def find_first_index_value(ls, value):
#     for index in range(len(ls) - 1, -1, -1):
#         if ls[index] == value:
#             return index
#
#     return -1
#
#
# def find_last_index_value(ls, value):
#     for index in range(len(ls)):
#         if ls[index] == value:
#             return index
#
#     return -1
#
#
# def count_value(ls, value):
#     count = 0
#
#     for item in ls:
#         if item == value:
#             count = count + 1
#     return count
#
#
# def main():
#     ls = []
#
#     print("input elements of list :")
#
#     while True:
#         number = input("element :")
#
#         if number == 'q':
#             break
#
#         ls.append(int(number))
#
#     value = int(input("input search value :"))
#
#     result = find_value(ls, value)
#
#     msg = "Yes" if result else "No"
#
#     print(msg)
#     print(ls)
#
# main()

# бинарный поиск в контейнере с упорядоченными элементами
# def search_element(ls, target):
#     a = 0
#     b = len(ls) - 1
#
#     while a <= b:
#         middle = (a + b) // 2
#         if ls[middle] == target:
#             return True
#         elif ls[middle] > target:
#             b = middle - 1
#         else:
#             a = middle + 1
#
#     return False
#
#
# def main():
#     ls = [5, 8, 12, 27, 29, 35, 39, 59, 62, 67, 77, 79, 89]
#     target = int(input("Input looking for digit: "))
#
#     result = search_element(ls, target)
#
#     msg = (f"Looking for digit {target} presents in {ls} list" if result == True
#            else f"Looking for digit {target} does not present in list")
#
#     print(msg)

# сортировка ОБМЕНА
# ls = [65, 38, 12, 257, 129, 35, 39, 5, 2, 67, 27, 39, 89, 23, 7]
# count = 0
# for j in range(len(ls) - 1):
#     flag = True
#     for i in range(len(ls) - 1 - j):
#         count = count + 1
#         if ls[i] > ls[i + 1]:
#             flag = False
#             t = ls[i]
#             ls[i] = ls[i + 1]
#             ls[i + 1] = t
#
#     if flag:
#         break
#
# print(ls)
# print("count =", count)

# сортировка ВЫБОРА
# ls = [65, 38, 12, 257, 129, 35, 39, 5, 2, 67, 27, 39, 89, 23, 7]
# count = 0
# for j in range(len(ls) - 1):
#     index_min_value = j
#
#     for i in range(j + 1, len(ls)):
#         count = count + 1
#         if ls[i] < ls[index_min_value]:
#             index_min_value = i
#     t = ls[j]
#     ls[j] = ls[index_min_value]
#     ls[index_min_value] = t
#
#
# print(ls)
# print(count)

# сортировка ВСТАВКИ
# ls = [65, 38, 12, 257, 129, 35, 39, 5, 2, 67, 27, 39, 89, 23, 7]
# count = 0
# for i in range(1, len(ls)):
#     item = ls[i]
#     j = i - 1
#
#     while item < ls[j] and j >= 0:
#         count = count + 1
#         ls[j + 1] = ls[j]
#         j = j - 1
#     ls[j+1] = item
#
# print(ls)
# print(count)

# сортировка встроенным оператором PYCharm
# ls = [65, 38, 12, 257, 129, 35, 39, 5, 2, 67, 27, 39, 89, 23, 7]
# ls.sort(reverse=True)
# print(ls)
#
# ls.sort()
# print(ls)

# проверка полиндрома
# def user_input():
#     num = list(input("Please enter a number for palindrome check: "))
#     return num
#
#
# def check_palindrome(number):
#     number_test = number[::-1]
#
#     return number == number_test
#
#
# def check_palindrome(num):
#     if isinstance(num, bool) or not isinstance(num, list):
#         return -1
#
#     num_copy = 0;
#
#     while num > 0:
#         num_copy *= 10
#         num_copy += num % 10
#         num //= 10
#
#     return num == num_copy
#
#
# def user_output(result):
#     msg = f"The number you've entered is {result}"
#     return msg
#
#
# def main():
#     num = user_input()
#     result = check_palindrome(num)
#     msg = user_output(result)
#     print(msg)
#
#
# main()
#
#
# def palindrom(number):
#     if number <= 0:
#         return -1
#     ls = []
#     while number > 0:
#         last_digit = number % 10
#         ls.append(last_digit)
#         number = number // 10
#
#     while len(ls) != 0:
#         if ls[0] != ls[len(ls) - 1]:
#             return False
#         ls = ls[1:len(ls) - 1]
#
#     return True
#
#
# def main():
#     number = int(input("Input your number: "))
#
#     result = palindrom(number)
#
#     msg = (f"Enter a natural number." if result == -1
#            else "Your number is a palindrome." if result
#     else f"Your number is not a palindrome.")
#
#     print(msg)
#
#
# main()

# поиск мин и макс количества букв в тексте
# import string
# str = """This year."""
#
# d = {}
# alfabet = string.ascii_lowercase
# s = str.lower()
#
# for ch in alfabet:
#     d[ch] = s.count(ch)
#
# # for key, value in d.items():
# #     print(key, " - ", value)
#
# max_key = "a"
# min_key = "a"
#
# for key in d:
#     if d[key] > d[max_key]:
#         max_key = key
#
#     if d[key] < d[min_key]:
#         min_key = key
#
# print(max_key, " - ", d[max_key])
# print(min_key, " - ", d[min_key])

