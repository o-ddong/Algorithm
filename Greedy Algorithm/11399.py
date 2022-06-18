# S4 ATM
# Greedy Algorithm

man = int(input())
takeTime = list(map(int, input().split()))
takeTime.sort()

for i in range(len(takeTime)-1):
    takeTime[i+1] += takeTime[i]

print(sum(takeTime))
