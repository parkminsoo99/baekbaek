number = int(input())
List = []
for _ in range(number):
    List.append(int(input()))
List.sort(reverse=True)
result = 0
count = number
for i in range(number):
    result += abs(count - List[i])
    count -= 1
print(result)
