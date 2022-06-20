# 얘는 수정해야됨

N = int(input())

alphabetList = [list(map(str, input())) for _ in range(N)]

alphabetList.sort()
maxValue = 9
alphabetSet = {}

# set value
for i in range(N):
    for j in range(len(alphabetList[i])):
        if alphabetList[i][j] not in alphabetSet:
            alphabetSet[alphabetList[i][j]] = str(maxValue)
            maxValue -= 1
    
# take a value
for i in range(N):
    for j in range(len(alphabetList[i])):
        alphabetList[i][j] = alphabetSet[alphabetList[i][j]]
    alphabetList[i] = int(''.join(alphabetList[i]))

print(sum(alphabetList))    
