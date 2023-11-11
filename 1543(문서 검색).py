import sys
List = list(map(str, sys.stdin.readline().rstrip()))
answer = list(map(str, sys.stdin.readline().rstrip()))
count = 0
i = 0
while (i != len(List)):
    if (i+len(answer) > len(List)):
        break
    if (len(answer) == 1):
        if (List[i] == answer[0]):
            count += 1
    else:
        if (List[i] == answer[0]):
            for a in range(1, len(answer)):
                if (List[i+a] != answer[a]):
                    break
                elif (a == len(answer)-1 and List[i+a] == answer[a]):
                    count += 1
                    i += len(answer)-1
    i += 1
print(count)
