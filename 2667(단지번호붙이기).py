import sys

number = int(input())
List = []
for _ in range(number):
    In = list(map(int, sys.stdin.readline().rstrip()))
    List.append(In)

x_list = [-1, 1, 0, 0]
y_list = [0, 0, -1, 1]
