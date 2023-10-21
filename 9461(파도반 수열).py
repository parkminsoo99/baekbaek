arr = [[]for _ in range(101)]
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 2

for i in range(6, len(arr)):
    arr[i] = arr[i-2] + arr[i-3]

num = int(input())
index = []
for i in range(num):
    index.append(int(input()))
for i in range(num):
    print(arr[index[i]])
