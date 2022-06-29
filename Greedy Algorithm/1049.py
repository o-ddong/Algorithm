# S4 기타줄

# 1번 풀이 (실패)
# 서로 다른 브랜드끼리 살 수 있는거를 고려를 하지 못함
n, m = map(int, input().split())
result = []

for i in range(m):
    package, one = map(int, input().split())

    if n <= 6:
        result.append(min(package, one * n))
    else:
        result.append(min((n // 6 + 1) * package, one * n, (n // 6 * package) + n % 6 * one))

print(min(result))

# 2번 풀이 (성공)

n, m = map(int, input().split())
packageMinValue = 1001
oneMinValue = 1001

for i in range(m):
    package, one = map(int, input().split())
    packageMinValue = min(packageMinValue, package) 
    oneMinValue = min(oneMinValue, one)

if n <= 6:
    print(min(packageMinValue, oneMinValue * n))
else:
    print(min((n // 6 + 1) * packageMinValue, oneMinValue * n ,(n // 6 * packageMinValue) + (n % 6) * oneMinValue))
