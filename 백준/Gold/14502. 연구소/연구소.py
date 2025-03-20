import sys
from collections import deque
import copy
N, M = map(int, sys.stdin.readline().split())
tempMap = []
maxSafeArea = 0
for _ in range(N):
    tempMap.append(list(map(int, sys.stdin.readline().split())))
#상 하 좌 우
positionList = [(0,-1),(0,1),(-1,0),(1,0)]

#바이러스 위치
positionVirus = []

#빈 위치
positionEmpty = []


#바이러스 위치 뽑기
for i in range(N):
    for j in range(M):
        if tempMap[i][j] == 2:
            positionVirus.append((i,j))
        elif tempMap[i][j] == 0:
            positionEmpty.append((i,j))

visited = [False for _ in range(len(positionEmpty))]
#바이러스 퍼트리기
def spreadVirus(tempMap):
    q = deque(positionVirus)
    countSafety = 0
    while q:
        popedX1, popedX2 = q.popleft()
        for tempX,tempY in positionList:
            x2 = popedX1 + tempX
            y2 = popedX2 + tempY
            if x2 >= 0 and y2 >= 0 and x2 < N and y2 < M and tempMap[x2][y2] == 0:
                    tempMap[x2][y2] = 2
                    q.append((x2,y2))
    for i in range(N):
        for j in range(M):
            if tempMap[i][j] == 0:
                countSafety +=1
    return countSafety

#벽 세우기
def wall(count,tempMap, visited):
    global maxSafeArea
    if count == 3:
        temp = spreadVirus(copy.deepcopy(tempMap))
        maxSafeArea = max(maxSafeArea, temp)
        return
    
    for i in range(len(positionEmpty)):
        if not visited[i]:
            visited[i] = True
            x1, y1 = positionEmpty[i]
            newMap = copy.deepcopy(tempMap)  # 맵을 복사해서 변경 사항이 개별적으로 적용되도록 함
            newMap[x1][y1] = 1  # 벽 세우기
            wall(count + 1, newMap, visited)
            visited[i] = False  # 원상 복구

for i in range(len(positionEmpty)):
    visited[i] = True
    x1, y1 = positionEmpty[i]
    newMap = copy.deepcopy(tempMap)
    newMap[x1][y1] = 1
    wall(1, newMap, visited)
    visited[i] = False

#결과 출력
print(maxSafeArea)