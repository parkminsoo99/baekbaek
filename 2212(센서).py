import sys
number = int(input())
K = int(input())
List = list(map(int, input().split()))
different = []
List.sort()
if (K > number):
    print(0)
    sys.exit()
for i in range(1, number):
    different.append(List[i]-List[i-1])
different.sort(reverse=True)
for i in range(K-1):
    different.pop(0)
print(sum(different))
