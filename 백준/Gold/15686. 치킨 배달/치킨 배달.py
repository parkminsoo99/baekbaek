import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
Map = []
for _ in range(N):
    Map.append(list(map(int, sys.stdin.readline().split())))
Chicken_List = []
Home_List = []
INF = 9999999
for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            Home_List.append((j+1, i+1))
        elif Map[i][j] == 2:
            Chicken_List.append((j+1, i+1))
        else:
            continue
result = []
for x in combinations(Chicken_List, M):
    sum = 0
    for i, j in Home_List:
        temp_min = 99999
        for count_x in range(M):
            Min = abs(i-x[count_x][0]) + abs(j-x[count_x][1])
            temp_min = min(temp_min, Min)
        sum += temp_min
    result.append(sum)
print(min(result))
