# S1 신입 사원
# 처음에 문제 접했을 때 이해를 잘 못했는데,
# 입력 받은 데이터를 점수로 생각했던 부분이랑
# 모든 지원자를 가리키는 말이 전체에 있어 다 비교하는 줄 알았는데
# 그러지 않고 입력 받은 순서대로 차례대로 비교하는 점이 가장 핵심이오따

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    rankList = []
    hired = 1

    for j in range(n):
        tmp = list(map(int, input().split()))
        rankList.append(tmp)
    
    rankList.sort(key=lambda x:x[0])
    min_Grade = rankList[0][1]

    for k in range(1, n):
        if min_Grade > rankList[k][1]:
            min_Grade = rankList[k][1]
            hired += 1
    
    print(hired)
