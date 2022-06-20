# S5 30
# 30의 배수 만들기

N = list(map(str, input()))
N.sort(reverse=True)
result = 0

for i in N:
    result += int(i)

if result % 3 != 0:
    print(-1)
elif N[-1] != '0':
    print(-1)
else:
    print(''.join(N))