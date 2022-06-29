# S1 행렬

def reverse_A(row, col):
    for i in range(row, row+3):
        for j in range(col, col+3):
            A[i][j] = 1 - A[i][j]

# row, col
n, m = map(int, input().split())
A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]
cnt = 0

for row in range(n-2):
    for col in range(m-2):
        if A[row][col] != B[row][col]:
            reverse_A(row, col)
            cnt += 1

if A == B:
    print(cnt)
else:
    print(-1)