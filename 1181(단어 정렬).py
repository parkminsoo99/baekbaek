import sys
sort = {}
num = int(sys.stdin.readline())
if (num < 0 or num > 20000):
    sys.exit(0)
for i in range(0, num):
    string = input()
    if (len(string) > 50 or len(string) <= 0):
        sys.exit(0)
    sort[string] = len(string)
sort = dict(sorted(sort.items()))
sort = dict(sorted(sort.items(), key=lambda x: x[1]))

my_list = list(sort.keys())
for i in my_list:
    print(i)
