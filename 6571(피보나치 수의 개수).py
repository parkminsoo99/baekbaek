import sys

result = []


def f(start, end):
    a = 1
    b = 2
    count = 0
    for i in range(3, 1001, 1):
        temp = a + b
        a, b = b, a
        b, temp = temp, b
        if (start <= temp and temp <= end):
            count = count + 1
        elif (temp > end):
            print(count)
            break


while (1):
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    if (num1 == 0 and num2 == 0):
        break
    print
    f(num1, num2)
