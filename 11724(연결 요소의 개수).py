from collections import deque
a, b = map(int, input().split())
List = [[] for _ in range(a+1)]
visit = [False] * (a+1)
for _ in range(b):
    c, d = map(int, input().split())
    List[c].append(d)
    List[d].append(c)


def dfs(start):
    visit[start] = True
    q = deque()
    q.append(start)
    while q:
        pop = q.popleft()
        for i in List[pop]:
            if not visit[i]:
                visit[i] = True
                q.append(i)


count = 0
for i in range(1, a+1):
    if (visit[i] != True):
        count += 1
        dfs(i)
print(count)
