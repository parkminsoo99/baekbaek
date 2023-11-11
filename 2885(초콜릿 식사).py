number = int(input())
choco = 1
List = []
while 1:
    if (choco >= number):
        break
    else:
        choco = choco * 2
count = 0
i = 0
orginal = choco
List.append(orginal)
while 1:
    if choco == 1:
        break
    List.append(int(choco / 2))
    choco = int(choco / 2)
for i in List:
    if (number % i == 0):
        break
    number = number % i
    count += 1
print(orginal, count)
