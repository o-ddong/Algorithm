# G2 저울
# 접근 방법이 너무 어려워서 다른 풀이 참고함

# endOfNum >= newNum 이면 endOfNum += newNum와 같이 끝을 연장할 수 있음
# 만약에 아니면, 성립이 안됨

n = int(input())
scaleweight = list(map(int, input().split()))

scaleweight.sort()
result = 0

for i in range(n):
    if result + 1 >= scaleweight[i]:
        result += scaleweight[i]
    else:
        break

print(result + 1)