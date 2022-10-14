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

# TASK 2 поиск суммы цифер заданого числа
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
#     print("input marks.\nFoe exit input -1\n")
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

# поиск максимального и минимального содержимого среди элементов контейнера с указанием номера контейнера
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

# TABLE OF PYTHAGORAS
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
