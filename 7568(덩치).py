
N = int(input())
a = [[] for _ in range(2)]

for i in range(N):
    x, y = map(int, input().split())
    a[0].append(x)
    a[1].append(y)
for i in range(N):
    rank = 1
    for j in range(N):
        if (a[0][i] < a[0][j] and a[1][i] < a[1][j]):
            rank += 1
    print(rank, end=" ")
