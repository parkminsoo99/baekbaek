number = int(input())
count = 0
temp = 0
while 1:
    if (number % 3 == 0):
        temp = number
        count_temp = count
    if (number // 5 > 0):
        number -= 5
        count += 1
    else:
        break
if (number == 0):
    print(count)
else:
    while 1:
        if (temp != 0):
            number = temp
            count = count_temp
        if (number % 3 == 0):
            count += (number // 3)
            print(count)
            break
        else:
            print(-1)
            break
