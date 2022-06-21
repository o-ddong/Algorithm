# G4 카드 정렬하기
# deque 풀이 (실패)
# 이유: 10 20 30 40 50 60 을 기준으로 생각해보면
# 30 30 40 50 60이 되고, 60 40 50 60이 되는데
# 더해지는 숫자들을 비교해 보았을 때 최적이 아님

# deque vs heap 차이
# deque는 양쪽에서 넣고 빼기 가능
# heapq는 특정 규칙(오름차순 or 내림차순)으로 정렬된 형태 유지

from collections import deque

# input
n = int(input())
cardSet = [int(input()) for _ in range(n)]

# sorting
cardSet = deque(sorted(cardSet))

result = 0

# calcultaion
while len(cardSet) != 1:
    first = cardSet.popleft()
    second = cardSet.popleft()
    result += first + second
    cardSet.appendleft(result)
    
print(result)

# 2번 풀이 (성공)
# heapq

import heapq

n = int(input())
result = 0

# heapq 선언하고 push 해주는 방식으로도 가능
cardSet = [int(input()) for _ in range(n)]
heapq.heapify(cardSet)

while len(cardSet) != 1:
    first = heapq.heappop(cardSet)
    second = heapq.heappop(cardSet)
    result += (first + second)
    heapq.heappush(cardSet, first + second)

print(result)

# deque로도 풀 수 있음
# http://boj.kr/d645477b0a364bcdbb13fe6ada989957
# http://boj.kr/fa9c168f4e744aa3bfd80a3f6d876b20