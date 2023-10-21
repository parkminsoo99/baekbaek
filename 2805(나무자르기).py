import sys
number1, number2 = map(int, sys.stdin.readline().split())
number_list = list(map(int, sys.stdin.readline().split()))
number_list.sort()
start = 1
end = max(number_list)
mid = 0
while (start <= end):
    mid = (start + end) // 2
    sum = 0
    for i in range(0, len(number_list)):
        if (number_list[i] > mid):
            sum = sum + (number_list[i] - mid)
    if (sum >= number2):
        start = mid + 1
    elif (sum < number2):
        end = mid - 1
print(end)
