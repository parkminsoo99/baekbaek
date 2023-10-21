from collections import deque


def bfs(i):
    c = 1
    queue = deque([i])
    tf = [False for _ in range(b+2)]
    tf[i] = True
    while queue:
        pop = queue.popleft()
        for i in graph[pop]:
            if not tf[i]:
                tf[i] = True
                queue.append(i)
                c += 1
    return c


a, b = map(int, input().split())
max = 1
answer = []

graph = [[]for _ in range(b+2)]
for _ in range(b):
    num1, num2 = map(int, input().split())
    graph[num2].append(num1)
for i in range(1, a+1, 1):
    count = bfs(i)
    if count > max:
        max = count
        answer.clear()
        answer.append(i)
    elif count == max:
        answer.append(i)
print(*answer)
