import sys
count_num = int(sys.stdin.readline())
num_list = {}

for i in range(0, count_num):
    num_list[i] = int(sys.stdin.readline())
num_list = dict(sorted(num_list.items(), key=lambda x: x[1], reverse=True))
for i in list(num_list.values()):
    print(i)
