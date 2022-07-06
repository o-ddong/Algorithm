# S2 BFS DFS
from collections import deque

def bfs(v):
    queue = deque()
    visited2[v] = 1
    queue.append(v)

    while queue:
        tmp = queue.popleft()
        print(tmp, end= ' ')
        for i in range(1, N+1):
            if visited2[i] == 0 and graph[tmp][i] == 1:
                queue.append(i)
                visited2[i] = 1

def dfs(v):
    visited[v] = 1
    print(v, end = ' ')

    for i in range(1, N+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (N + 1)
visited2 = [0] * (N + 1)

dfs(V)
print()
bfs(V)