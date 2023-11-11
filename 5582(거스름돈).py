number = int(input())
key = [500, 100, 50, 10, 5, 1]
pay = 1000 - number
count = 0
for i in key:
    while (pay // i != 0):
        pay -= i
        count += 1
print(count)
