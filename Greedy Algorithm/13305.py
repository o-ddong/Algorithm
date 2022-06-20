# S4 주유소
# Greedy Algorithm

# 1번 해설
n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

priceMin = min(price[:-1])
result = road[0] * price[0]

for i in range(len(road)):
    if price[i] == priceMin:
        result += (sum(road[i:]) * price[i])
        break
    else:
        result += road[i] * price[i]

print(result)

# 2번 해설
N = int(input())

roads = list(map(int,input().split()))
costs = list(map(int,input().split()))

# 첫번째 값 더하기
min_price = roads[0] * costs[0]

# 가장 값이 싼 주유소 지정
min_cost = costs[0]

for i in range(1, N-1):
  if min_cost > costs[i]: # 가장 값이 싼 주유소가 현재 주유소 보다 비싸면 바꿔준다.
    min_cost = costs[i] # 값 싼 주유소로 바꿔주기
  
  min_price += min_cost * roads[i]

print(min_price)