import sys
from collections import deque


def bfs(start):
    queue = deque([start])
    tf = [False for _ in range(a+1)]
    tf[start] = True
    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        for i in bfs_graph[pop]:
            if not tf[i]:
                tf[i] = True
                queue.append(i)


def dfs(start, tf_dfs):
    tf_dfs[start] = True
    print(start, end=' ')
    for i in dfs_graph[start]:
        if not tf_dfs[i]:
            dfs(i, tf_dfs)


a, b, c = map(int, sys.stdin.readline().split())
bfs_graph = [[] for _ in range(a+1)]
dfs_graph = [[] for _ in range(a+1)]
tf_dfs = [False for _ in range(a+1)]
for _ in range(b):
    x, y = map(int, sys.stdin.readline().split())
    bfs_graph[x].append(y)
    bfs_graph[y].append(x)
    dfs_graph[x].append(y)
    dfs_graph[y].append(x)
for i in range(1, a+1):
    bfs_graph[i].sort()
    dfs_graph[i].sort()
dfs(c, tf_dfs)
print()
bfs(c)
