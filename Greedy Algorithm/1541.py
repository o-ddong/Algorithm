# S2 잃어버린 괄호
# 그리디 알고리즘이라기보다는 

n = input().split('-')
ans = 0

for i in n[0].split('+'):
    ans += int(i)

for i in n[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)