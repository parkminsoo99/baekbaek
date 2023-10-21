import sys
count0 = 0
count1 = 0
num0_list = [[0 for col in range(41)] for row in range(2)]
num0_list[0][0] = 0
num0_list[0][1] = 1
num0_list[0][2] = 1
num0_list[0][3] = 2
# --------------------
num0_list[1][0] = 1
num0_list[1][1] = 0
num0_list[1][2] = 0
num0_list[1][3] = 1
num_list = []
num1 = int(sys.stdin.readline())
if (num1 <= 0):
    sys.exit(0)
for i in range(0, num1):
    num2 = int(sys.stdin.readline())
    if (num2 < 0 or num2 > 40):
        sys.exit(0)
    num_list.append(num2)
for a in range(4, max(num_list)+1):
    num0_list[0][a] = num0_list[0][a-1] + num0_list[0][a-2]
for j in num_list:
    if (j == 0):
        print(num0_list[0][j+1], end='')
        print(' ', end='')
        print(num0_list[0][j])
    else:
        print(num0_list[0][j-1], end='')
        print(' ', end='')
        print(num0_list[0][j])
