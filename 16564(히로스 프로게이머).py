import sys
number1, number2 = map(int, sys.stdin.readline().split())
number1_list = []
number2_list = []
for i in range(0, number1):
    number1_list.append(int(sys.stdin.readline()))
number1_list.sort()
number2_list.append(min(number1_list))
number1_list.remove(min(number1_list))
while (len(number2_list) <= number2):
    if (len(number1_list) > 0):
        plus = number1_list[0] - number2_list[0]
        minus_level = plus * len(number2_list)
        if (minus_level <= number2):  # 최소값끼리 한 번에 추가
            number2 = number2 - minus_level
            for i in range(0, len(number2_list)):
                number2_list[i] = number2_list[i] + plus
            number2_list.append(min(number1_list))
            number1_list.remove(min(number1_list))
        else:  # 1씩 추가
            for i in range(0, len(number2_list)):
                number2_list[i] = number2_list[i] + 1
                number2 = number2 - 1
    else:
        for i in range(0, len(number2_list)):
            number2_list[i] = number2_list[i] + 1
            number2 = number2 - 1
print(number2_list[0])
