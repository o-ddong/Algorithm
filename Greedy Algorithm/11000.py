# G5 강의실 배정

# 1번 풀이 (틀림)
# 정렬을 안하고 입력을 받는 것은
# 3
# 3 5
# 2 4
# 1 3
# 와 같은 경우 기댓값 2가 나와야 하는데 3이 나오게 됨

import heapq

N = int(input())
room = []

for i in range(N):
    start, end = map(int, input().split())

    if len(room) == 0:
        heapq.heappush(room, end)
    elif room[0] <= start:
        heapq.heappop(room)
        heapq.heappush(room, end)
    else:
        heapq.heappush(room, end)

print(len(room))


# 2번 풀이 (성공)
import heapq, sys
input = sys.stdin.readline

N = int(input())
tmpList = []

for i in range(N):
    tmpList.append(list(map(int, input().split())))

tmpList.sort()
room = []
heapq.heappush(room, tmpList[0][1])

for i in range(1, N):
    if room[0] <= tmpList[i][0]: # 끝나는 시간 <= 새롭게 시작하는 시간
        heapq.heappop(room)
        heapq.heappush(room, tmpList[i][1])
    else:
        heapq.heappush(room, tmpList[i][1])

print(len(room))