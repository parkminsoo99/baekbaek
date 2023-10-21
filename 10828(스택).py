import sys
iteration = int(sys.stdin.readline())
stack = []
correct = []
for i in range(0, iteration):
    command = list(map(str, sys.stdin.readline().split()))
    if (len(command) == 1):
        if (command[0] == "top"):
            if (len(stack) == 0):
                correct.append("-1")
            else:
                correct.append(stack[len(stack)-1])
        elif (command[0] == "pop"):
            if (len(stack) == 0):
                correct.append("-1")
            else:
                correct.append(stack.pop(len(stack)-1))
        elif (command[0] == "size"):
            correct.append(len(stack))
        elif (command[0] == "empty"):
            if (len(stack) == 0):
                correct.append("1")
            else:
                correct.append("0")
    else:
        stack.append(command[1])
for j in correct:
    print(j)
