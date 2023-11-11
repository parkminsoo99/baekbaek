from collections import deque
import heapq
a, b = map(int, input().split())
List = []
graph = [[] for _ in range(a+1)]
inorder = [0] * (a+1)
for i in range(b):
    List.append(list(map(int, input().split())))
for i in range(b):
    for j in range(2, len(List[i])):
        inorder[List[i][j]] += 1

for i in range(b):
    for j in range(1, len(List[i])-1):
        graph[List[i][j]].append(List[i][j+1])


def to():
    result = []
    heap = []
    for i in range(1, a+1):
        if inorder[i] == 0:
            heapq.heappush(heap, i)
    while heap:
        now = heapq.heappop(heap)
        result.append(now)
        for i in graph[now]:
            inorder[i] -= 1
            if (inorder[i] == 0):
                heapq.heappush(heap, i)
    if len(result) != a:
        print(0)
    else:
        for i in result:
            print(i)


to()
