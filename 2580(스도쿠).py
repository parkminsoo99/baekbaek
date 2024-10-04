import time
#스도쿠
import sys
S = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]
# for _ in range(9):
#     S.append(list(map(int, sys.stdin.readline().split())))

def solutions(map):
    def is_valid(target, row, col):
        
        # 같은 행(row)에 중복된 숫자가 있는지 확인
        if target in map[row]:
            return False
        # 같은 열(col)에 중복된 숫자가 있는지 확인
        if target in [map[i][col] for i in range(9)]:
            return False
        # 3x3 박스 안에 중복된 숫자가 있는지 확인
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if map[i][j] == target:
                    return False
        return True

    def find_empty():
        for i in range(9):
            for j in range(9):
                if map[i][j] == 0:
                    return i, j
        return False

    def find_solution():
        is_empty = find_empty()
        if not is_empty:
            return True
        row, col = is_empty
        for i in range(1, 10):
            if is_valid(i, row, col): 
                time.sleep(1)
                print(map[row][col], i)
                map[row][col] = i
                if find_solution():
                    print("1")
                    return True
                map[row][col] = 0
                for i in range(9):
                    print(*map[i])
        return False
    find_solution()
    return map

result = solutions(S)
for i in range(9):
    print(*result[i])
