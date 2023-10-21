import sys
a = 1
b = 2
num1 = int(sys.stdin.readline())
count = 0
if (num1 == 0):
    print(0)
    sys.exit(0)
if (num1 == 1 or num1 == 2):
    print(a)
    sys.exit(0)
for z in range(2, num1+1):
    temp = a + b
    a, b = b, a
    b, temp = temp, b
print(temp, end='')
print(' ', end='')
