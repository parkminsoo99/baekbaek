
from collections import deque
import copy
N, M, V = map(int, input().split())

visited = [False for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1):
    graph[i].sort()


def dfs(visited, graph, V):
    visited[V] = True
    print(V, end=' ')
    for i in graph[V]:
        if not visited[i]:
            visited[i] = True
            dfs(visited, graph, i)


dfs(copy.deepcopy(visited), graph, V)

print()


def bfs(visited, graph, V):
    q = deque([V])
    visited[V] = True
    while q:
        poped = q.popleft()
        print(poped, end=' ')
        for i in graph[poped]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


bfs(copy.deepcopy(visited), graph, V)