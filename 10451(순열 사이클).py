from collections import deque


def bfs(start, Is):
    if ([start] == array[start] and Is[start] == False):
        return 1
    queue = deque()
    queue.append(start)
    Is[start] = True
    while queue:
        pop = queue.popleft()
        for i in array[pop]:
            if (i == start):
                return 1
            if not Is[i]:
                Is[i] = True
                queue.append(i)
            else:
                return 0
    return 1


a = int(input())
answer = []
for _ in range(a):
    b = int(input())
    Is = [False for _ in range(b+1)]
    array = [[] for _ in range(b+1)]
    Input = list(map(int, input().split()))
    count = 0
    for i in range(b):
        array[i+1].append(Input[i])
    for i in range(1, b+1, 1):
        tf = bfs(i, Is)
        if (tf == 1):
            count += 1
        else:
            continue
    answer.append(count)
for i in answer:
    print(i)
