import sys
num0_list = [0 for col in range(100001)]
num0_list[0] = 0
num0_list[1] = 1
num0_list[2] = 1
num0_list[3] = 2
num1 = int(sys.stdin.readline())
if (num1 < 0 or num1 > 10000):
    sys.exit(0)
for a in range(4, num1+1):
    num0_list[a] = num0_list[a-1] + num0_list[a-2]
print(num0_list[num1])
