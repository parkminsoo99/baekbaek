from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            start_x = x + x_list[i]
            start_y = y + y_list[i]
            if (start_x < 0 or start_y < 0 or start_x >= b or start_y >= a):
                continue
            if (graph[start_y][start_x] == 0):
                continue
            if (graph[start_y][start_x] == 1):
                graph[start_y][start_x] = graph[y][x] + 1
                queue.append((start_y, start_x))
    return graph[a - 1][b - 1]


a, b = map(int, input().split())
x_list = [1, -1, 0, 0]
y_list = [0, 0, 1, -1]
graph = []
for _ in range(a):
    graph.append(list(map(int, input())))

print(bfs(0, 0))
