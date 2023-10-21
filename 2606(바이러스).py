import sys
from collections import deque


def bfs(start):
    count = 0
    queue = deque([start])
    tf = [False for _ in range(a+1)]
    tf[start] = True
    while queue:
        pop = queue.popleft()
        for i in List[pop]:
            if not tf[i]:
                queue.append(i)
                tf[i] = True
                count += 1
    return count


a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
List = [[] for _ in range(a+1)]

for i in range(b):
    x, y = map(int, sys.stdin.readline().split())
    List[x].append(y)
    List[y].append(x)
count = bfs(1)
print(count)
