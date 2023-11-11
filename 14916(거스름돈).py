import sys
number = int(input())
count = 0
if (number == 1 or number == 3):
    print(-1)
    sys.exit(0)
if (number == 2 or number == 5):
    print(1)
    sys.exit(0)
if (number == 4):
    print(2)
    sys.exit(0)
while 1:
    number -= 5
    count += 1
    if (number // 5 == 0 and number % 2 != 0):
        number = number + 5
        count -= 1
        break
    if (number // 5 == 0):
        break
while (number // 2 != 0):
    number = number - 2
    count += 1
print(count)


# 만약 5를 빼고나서 8인데, 5로 나눠서 몫이 1이고, 2로 나눠지지 않는다면 +5
