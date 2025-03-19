import sys
N = map(int, sys.stdin.readline().split())
N_List = list(map(int, sys.stdin.readline().split()))
M =  map(int, sys.stdin.readline().split())
M_List = list(map(int, sys.stdin.readline().split()))

hashMap = {}
for i in N_List:
    if i in hashMap:
        hashMap[i] += 1
    else:
        hashMap[i] = 0

for i in M_List:
    if i in hashMap:
        print(1)
    else:
        print(0)