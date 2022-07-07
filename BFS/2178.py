# S1 미로 탐색

# 1번 풀이 (성공)
# 다만 방문 checking을 할 필요가 없음

from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    
    # 상 하 좌 우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [([0] * m) for _ in range(n)]

bfs()

print(graph[n-1][m-1])

# 2번 풀이 (성공)

from collections import deque

n, m = map(int, input().split())

# 칸 입력
graph = [list(map(int, input())) for _ in range(n)]

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))