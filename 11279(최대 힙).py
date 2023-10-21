import sys
import heapq
from collections import deque
iteration = int(sys.stdin.readline())
dq = deque()
heap = []
for i in range(0, iteration):
    input = int(sys.stdin.readline())
    if (input == 0 and len(heap) != 0):
        dq.append(-heapq.heappop(heap))
    elif (input == 0 and len(heap) == 0):
        dq.append(0)
    else:
        heapq.heappush(heap, -input)
for i in range(0, len(dq)):
    print(dq.popleft())
