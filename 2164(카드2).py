import sys
from collections import deque
number = int(sys.stdin.readline())
dp = deque()
for i in range(1, number+1):
    dp.append(i)
while (len(dp) != 1):
    dp.popleft()
    dp.append(dp.popleft())
print(dp.popleft())
