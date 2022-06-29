# G4 수 묶기
# 0, plus => 덧셈
# 0, minus => 곱셈

# 1, plus => 덧셈
# 1, minus => 덧셈

# p, p => 곱셈
# m, m => 곱셈
# p, m => 덧셈

n = int(input())

minusList = []
plusList = []
result = 0

for i in range(n):
    tmp = int(input())
    if tmp > 1:
        plusList.append(tmp)
    elif tmp == 1:
        result += 1
    else:
        minusList.append(tmp)

plusList.sort(reverse=True)
minusList.sort()

# Plus 개수가 짝수개일 때
if len(plusList) % 2 == 0:
    for i in range(0, len(plusList), 2):
        result += plusList[i] * plusList[i+1]
else: # 홀수
    for i in range(0, len(plusList)-1, 2):
        result += plusList[i] * plusList[i+1]
    result += plusList[-1]

# minus 개수가 짝수개일 때
if len(minusList) % 2 == 0:
    for i in range(0, len(minusList), 2):
        result += minusList[i] * minusList[i+1]
else: # 홀수
    for i in range(0, len(minusList)-1, 2):
        result += minusList[i] * minusList[i+1]
    result += minusList[-1]

print(result)