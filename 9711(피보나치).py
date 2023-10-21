import sys
number = 1
result = []


def f(num1):
    a = 1
    b = 1
    if (num1 < 0):
        sys.exit(0)
    for z in range(0, num1):
        temp = a + b
        a, b = b, a
        b, temp = temp, b
    return temp


num1 = int(sys.stdin.readline())

for i in range(0, num1):
    num2, num3 = input().split()
    num2 = int(num2)
    num3 = int(num3)
    if (num2 > 10000 or num2 < 1 or num3 < 1 or num3 > 2000000000):
        sys.exit(0)
    tmp1 = f(num2)
    result.append(tmp1 % num3)

for i in result:
    print('Case #', end='')
    print(number, end='')
    print(':', i)
    number = number + 1
