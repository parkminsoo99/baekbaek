import sys
literation = int(sys.stdin.readline())
correct = []
for a in range(0, literation):
    count_1 = 0
    count_2 = 0
    already = 0
    List = input()
    List = list(List)
    for i in List:
        if (count_1 < count_2):
            correct.append("NO")
            already = 1
            break
        if (i == '('):
            count_1 = count_1 + 1
        else:
            count_2 = count_2 + 1
    if (count_1 == count_2):
        correct.append("YES")
    elif (count_1 != count_2 and already != 1):
        correct.append("NO")
for j in correct:
    print(j)
