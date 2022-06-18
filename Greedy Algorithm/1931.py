# S1 회의실 배정
# 정렬 알고리즘 key=lambda를 이용한 문제 해결 방법이 핵심임


n = int(input())
meetingTime = [list(map(int, input().split())) for _ in range(n)]
    
meetingTime.sort(key=lambda a:(a[0]))
meetingTime.sort(key=lambda a:(a[1]))
cnt = 0

start_Time = 0 # 시작하는 시간
last_Time = 0 # 끝나는 시간
for i, (start, end) in enumerate(meetingTime):
    # 시작하는 시간은 전의 끝났던 시간보다 같거나 커야하고 
    if start >= last_Time:
        last_Time = end
        cnt += 1

print(cnt)

