import sys
from collections import deque
def bfs(start,visited):
    q = deque([start])
    visited[start] = True
    while q:
        pop = q.popleft()
        print(pop, end=' ')
        for i in graph[pop]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
def dfs(start, visited):
    print(start,end=' ')
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i, visited)
N, M, V = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    x, y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(len(graph)):
    graph[i].sort()
dfs(V, visited.copy())
print()
bfs(V, visited.copy())