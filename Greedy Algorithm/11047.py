# S4 동전0
# Greedy Algorithm

N, money = map(int, input().split())
money_Value = [int(input()) for _ in range(N)]
moeny_Value = money_Value.reverse()
cnt = 0
# print(N ,money, money_Value)

for i in money_Value:
    cnt += money // i
    money %= i

print(cnt)