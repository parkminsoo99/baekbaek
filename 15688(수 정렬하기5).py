import sys
n = int(sys.stdin.readline())

arr = {}
for i in range(-1000000, 1000001):
    arr[i] = 0
for i in range(0, n):
    k = int(sys.stdin.readline())
    arr[k] += 1

for i in range(-1000000, 1000001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
    del arr[i]
