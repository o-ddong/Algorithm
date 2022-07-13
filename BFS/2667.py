# S1 단지번호 붙이기

# 1번 풀이 (성공) - 큐 사용

from collections import deque

def bfs(x, y):
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if visited[nx][ny] == 1:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = num
                visited[nx][ny] = 1
                cnt += 1
    
    result[num] = cnt
    return result

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

visited = [[0] * (n + 1) for _ in range(n)]
result = {}
num = 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            num += 1

print(len(result))
result = sorted(result.items(), key = lambda item:item[1])
for i in result:
    print(i[1])

# 2번 풀이 (성공) - 재귀

def dfs(x, y):
    global num
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    
    if graph[x][y] == 0:
        return
    
    graph[x][y] = 0
    num += 1

    dfs(x+1, y) # 상 
    dfs(x-1, y) # 하
    dfs(x, y-1) # 좌
    dfs(x, y+1) # 우

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
cnt = []
num = 0
result = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i, j)
            if num > 0:
                result += 1
                cnt.append(num)
                num = 0
print(result)
cnt.sort()
for i in cnt:
    print(i)
