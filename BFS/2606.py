# S3 바이러스

from collections import deque

def bfs(k):
    queue = deque()
    queue.append(k)
    visited[k] = 1
    cnt = 0

    while queue:
        v = queue.popleft()

        for i in range(computerCount+1):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                cnt += 1
    
    return cnt

# com Count, com node
computerCount = int(input())
computerConnectCount = int(input())

visited = [0] * (computerCount + 1)
graph = [[0] * (computerCount + 1) for _ in range(computerCount+1)]

for i in range(computerConnectCount):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

print(bfs(1))