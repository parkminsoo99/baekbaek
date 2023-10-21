import sys

result = []


def f(num1):
    a = 1
    b = 2
    for z in range(2, pow(10, 21000)+1):
        temp = a + b
        a, b = b, a
        b, temp = temp, b
        if (num1 == temp):
            return z


num1 = int(sys.stdin.readline())
count = 0
if (num1 < 1 or num1 > 100000):
    sys.exit(0)
for i in range(0, num1):
    num2 = int(sys.stdin.readline())
    n = f(num2)
    result.append(n)
for i in result:
    print(i)
