# S4 보물

n = int(input())
A_List = list(map(int, input().split()))
B_List = list(map(int, input().split()))

A_List.sort(reverse=True)
B_List.sort()

for i in range(n):
    B_List[i] *= A_List[i]

print(sum(B_List))