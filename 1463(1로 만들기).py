import sys

limit = 10 * 10 * 10 * 10 * 10 * 10
number = int(sys.stdin.readline())
if (number < 1 or number > limit):
    sys.exit(0)
x = {1: 1, 2: 1, 3: 1}
y = {1: 1, 2: 1, 3: 1}
count = 0
result_value = []
first_value = 0
second_value = 0
if (number == 1):
    print(0)
    sys.exit(0)
if (number == 2 or number == 3):
    print(x[number])
    sys.exit(0)
for i in range(4, number+1):
    result_value = []
    if (i % 2 != 0 and i % 3 != 0):
        count = 0
        count += 1
        div_number = i - 1
        count += x[div_number]
        x[i] = count
    elif (i % 3 == 0 and i % 2 == 0):
        count1 = 0
        count2 = 0
        div_number1 = i / 2
        count1 += 1
        count1 += x[div_number1]
        div_number2 = i / 3
        count2 += 1
        count2 += x[div_number2]
        if (count1 < count2):
            x[i] = count1
        else:
            x[i] = count2
        if (x[i] - x[i-1] >= 2):
            count = 0
            count += 1
            div_number = i - 1
            count += x[div_number]
            x[i] = count
    elif (i % 2 == 0):
        count = 0
        div_number = i / 2
        count += 1
        count += x[div_number]
        x[i] = count
        if (x[i] - x[i-1] >= 2):
            count = 0
            count += 1
            div_number = i - 1
            count += x[div_number]
            x[i] = count
    elif (i % 3 == 0):
        count = 0
        div_number = i / 3
        count += 1
        count += x[div_number]
        x[i] = count
        if (x[i] - x[i-1] >= 2):
            count = 0
            count += 1
            div_number = i - 1
            count += x[div_number]
            x[i] = count
print(x[number])
