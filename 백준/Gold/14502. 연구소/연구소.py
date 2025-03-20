
import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())
tempMap = []
for _ in range(N):
    tempMap.append(list(map(int, sys.stdin.readline().split())))

# 상하좌우 이동
positionList = [(0,-1), (0,1), (-1,0), (1,0)]

# 바이러스 위치 및 빈 공간 위치 저장
positionVirus = []
positionEmpty = []

for i in range(N):
    for j in range(M):
        if tempMap[i][j] == 2:
            positionVirus.append((i, j))
        elif tempMap[i][j] == 0:
            positionEmpty.append((i, j))

visited = [False] * len(positionEmpty)
maxSafeArea = 0  # 최대 안전 영역 저장


# 바이러스 퍼트리기
def spreadVirus(tempMap):
    q = deque(positionVirus)  # 모든 바이러스 위치에서 시작
    while q:
        popedX1, popedX2 = q.popleft()
        for tempX, tempY in positionList:
            x2, y2 = popedX1 + tempX, popedX2 + tempY
            if 0 <= x2 < N and 0 <= y2 < M and tempMap[x2][y2] == 0:
                tempMap[x2][y2] = 2
                q.append((x2, y2))

    return sum(row.count(0) for row in tempMap)  # 안전 영역 개수 반환


# 벽 세우기
def wall(count, tempMap, visited):
    global maxSafeArea
    if count == 3:
        temp = spreadVirus(copy.deepcopy(tempMap))
        maxSafeArea = max(maxSafeArea, temp)
        return
    
    for i in range(len(positionEmpty)):
        if not visited[i]:
            visited[i] = True
            x1, y1 = positionEmpty[i]
            newMap = copy.deepcopy(tempMap)
            newMap[x1][y1] = 1  # 벽 세우기
            wall(count + 1, newMap, visited)
            visited[i] = False  # 원상 복구


# 벽을 세울 3개 위치 선택 (백트래킹)
for i in range(len(positionEmpty)):
    visited[i] = True
    x1, y1 = positionEmpty[i]
    newMap = copy.deepcopy(tempMap)
    newMap[x1][y1] = 1
    wall(1, newMap, visited)  # count=1부터 시작
    visited[i] = False

# 결과 출력
print(maxSafeArea)
