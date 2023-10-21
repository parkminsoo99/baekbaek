import sys
from collections import deque
number1, number2 = map(int, sys.stdin.readline().split())
dq = deque()
for i in range(1, number1+1):
    dq.append(i)
print(end='<')
while (len(dq) != 0):
    dq.rotate(-number2+1)
    if (len(dq) != 1):
        print(dq.popleft(), end=', ')
    else:
        print(dq.popleft(), end='')
print(end='>')
