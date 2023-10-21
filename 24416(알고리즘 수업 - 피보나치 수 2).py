import sys
limit = pow(10, 8)
limit = limit * 2
a = 1
b = 2
num1 = int(sys.stdin.readline())
count = 0
if (num1 < 5 or num1 > limit+1):
    sys.exit(0)
for z in range(2, num1+1):
    temp = a + b
    if (temp > 1000000006):
        temp = temp - 1000000007
    a, b = b, a
    b, temp = temp, b
print(temp, end='')
print(' ', end='')
print(num1 - 2)
