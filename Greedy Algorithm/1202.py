# G2 보석 도둑
# 최대 가격을 구해야하니 가격 중심으로 정렬을 해주어야 됨

# 1번 풀이 (실패)
# 가방 크기에 따른 보석 무게를 고려하지 않아 틀려씀

# n, k = map(int, input().split())
# result = 0

# # 보석 정보랑 훔치는 가방 정보 입력
# jewelList = [list(map(int, input().split())) for _ in range(n)]
# bagList = [int(input()) for _ in range(k)]

# # 보석 정보들을 가격 비싼순으로 정렬
# jewelList.sort(key=lambda x:(x[1], x[0]), reverse=True)

# # 
# for i in range(k):
#     for j in range(i, n):
#         if bagList[i] >= jewelList[j][0]:
#             result += jewelList[j][1]
#             break

# print(result)


# 2번 풀이 (실패)
# 가방 크기를 고려 못했음 humm...

# import heapq

# # 1. input 선언
# n, k = map(int, input().split())

# # 2. heap으로 jewel 등록하고
# jewelList = [list(map(int, input().split())) for _ in range(n)]
# bagList = [int(input()) for _ in range(k)]
# jewelHeapList = []
# result = 0

# # -가격, 무게, 가격 (최대 힙)
# for jewel in jewelList:
#     heapq.heappush(jewelHeapList, (-jewel[1], jewel[0], jewel[1]))

# # 3. 가방 최대값이 앞으로 오게 정렬
# bagList.sort(reverse=True)

# # 4. 가방 - jewel 가격 높은애 check
# for i in range(len(bagList)):
#     while True:
#         if len(jewelHeapList) > 0:
#             tmp = heapq.heappop(jewelHeapList)
#             if bagList[i] >= tmp[1]:
#                 result += tmp[2]
#                 break
#         else:
#             break
    
# print(result)

# 3번 풀이

import heapq, sys
input = sys.stdin.readline

# 1. input 선언
n, k = map(int, input().split())
jewelList = [list(map(int, input().split())) for _ in range(n)]
bagList = [int(input()) for _ in range(k)]

# 2. jewel-bag 비교 편하게 sorting
jewelList.sort()
bagList.sort()

# 3. output data
jewelHeapList = []
result = 0

# 4. 앞서 가방의 크기를 고려하지 못해 틀렸는데
# 가방에 넣을 수 있는 무게라면 일단 모두 추가하고, 그 개수만큼만 최대 힙을 이용해 result에 담는 방법

for i in bagList:
    while jewelList and i >= jewelList[0][0]:
        heapq.heappush(jewelHeapList, -jewelList[0][1])
        heapq.heappop(jewelList)
    
    if jewelHeapList:
        result += heapq.heappop(jewelHeapList)
    elif not jewelList: 
        break

print(-result)