
import heapq
a, b = map(int, input().split())
graph = [[] for _ in range(a+1)]
follow = [0] * (a+1)
for i in range(b):
    x, y = map(int, input().split())
    graph[x].append(y)
    follow[y] += 1


def to():
    result = []
    heap = []
    for i in range(1, a+1):
        if (follow[i] == 0):
            heapq.heappush(heap, i)
    print(heap)
    while heap:
        now = heapq.heappop(heap)
        result.append(now)
        for i in graph[now]:
            follow[i] -= 1
            if follow[i] == 0:
                heapq.heappush(heap, i)
                print(heap, i)
    for i in result:
        print(i, end=' ')


to()
