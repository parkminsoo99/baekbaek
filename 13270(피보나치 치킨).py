import sys
num1 = int(sys.stdin.readline())
if (num1 < 2):
    sys.exit(0)
a = (num1+1)/2
b = (num1*2)/3
print(int(a), int(b))
