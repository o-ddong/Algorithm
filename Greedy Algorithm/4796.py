# S5 캠핑
# if - else 나누는 부분 틀리고나서 인지했다 !!

L, P, V = map(int, input().split())
i = 1

while L * P * V != 0:
    if V % P <= L:
        print(f'Case {i}:' , (L * (V//P)) + (V % P))
    else:
        print(f'Case {i}:' , (L * (V//P)) + L)
    i += 1
    L, P, V = map(int, input().split())