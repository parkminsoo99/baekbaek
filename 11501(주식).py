import sys
number = int(sys.stdin.readline())
List = []
for i in range(number):
    days = int(sys.stdin.readline())
    result = 0
    Max = 0
    List = list(map(int, sys.stdin.readline().split()))
    for i in range(len(List)-1, -1, -1):
        if (Max < List[i]):
            Max = List[i]
        else:
            result += Max - List[i]
    print(result)
