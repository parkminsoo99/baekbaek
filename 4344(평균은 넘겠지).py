import sys
number_list = []
sum = 0
count = 0
number1 = int(sys.stdin.readline())
for i in range(0, number1):
    number_list = list(map(int, input().split()))
    for j in range(1, number_list[0]+1):
        sum = sum + number_list[j]
    average = sum / number_list[0]
    for a in range(1, number_list[0]+1):
        if (int(average) < number_list[a]):
            count = count + 1
    print(round((100 / number_list[0] * count), 3), end='')
    print("%")
    sum = 0
    average = 0
    count = 0
    number_list = []
