# G4 단어수학
# 접근하기 조금 어려웠음
# 런타임에러(KeyError) 마주함
# 이유: 입력에서 10개의 문자만 주어진다해 alphabetList를 A ~ J까지 설정하고 했지만,
# A ~ J까지만 들어온다는 보장이 없었다. 
# 만약에 Z같은 문자가 들어온다면 dict을 초기 설정해주는 code가 존재하지 않아 KeyError가 발생한 것이다.

# set input data
alphabetDict = {}
n = int(input())
alphabetList = [list(map(str, input())) for _ in range(n)]
maxValue = 9

# set Dict
for i in range(n):
    for j in range(len(alphabetList[i])):
        if alphabetList[i][j] in alphabetDict:
            alphabetDict[alphabetList[i][j]] += 10 ** (len(alphabetList[i]) - j - 1)
        else:
            alphabetDict[alphabetList[i][j]] = 10 ** (len(alphabetList[i]) - j - 1)

# save value from Dict to result
result = []
for value in alphabetDict.values():
    if value > 0:
        result.append(value)

# sorting
result.sort(reverse=True)

# Calculation
for i in range(len(result)):
    result[i] *= (maxValue - i)

print(sum(result))