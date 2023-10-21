import sys

result = []
result.append(1)
result.append(1)
result.append(1)


def f(num1):
    for i in range(3, num1):
        result.append(result[i-1] + result[i-3])
    print(result[num1-1])


num1 = int(sys.stdin.readline())
if (num1 < 1 or num1 > 116):
    sys.exit(0)
if (num1 == 1 or num1 == 2):
    print(1)
    sys.exit(0)
f(num1)
