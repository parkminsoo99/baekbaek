number = int(input())
List = []
dp = [1] * (number)
for _ in range(number):
    i = int(input())
    List.append(i)

for i in range(number):
    for j in range(i):
        if (List[i] > List[j]):
            dp[i] = max(dp[i], dp[j]+1)
print(number - max(dp))
