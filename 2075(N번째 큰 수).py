import sys

number = int(sys.stdin.readline())
number_list = []
result_list = []
for i in range(0, number):
    number_list = list(map(int, input().split()))
    if (i == 0):
        result_list = number_list
        result_list.sort()
    else:
        for j in number_list:
            if (result_list[0] < j):
                result_list[0] = j
                result_list.sort()
print(result_list[0])
