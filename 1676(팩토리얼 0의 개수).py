import sys
number1 = int(sys.stdin.readline())
a = 1
count = 0
list1 = []
for i in range(number1, 0, -1):
    a = a * i
list1 = list(map(int, str(a)))
list1.reverse()
for i in list1:
    if (i == 0):
        count = count + 1
        continue
    break
print(count)
