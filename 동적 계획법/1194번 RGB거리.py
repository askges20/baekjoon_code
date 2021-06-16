n=int(input())
p=list(map(int,input().split()))
cost=p
for i in range(n-1):
    p=list(map(int,input().split()))
    cost=[min(cost[1],cost[2])+p[0], min(cost[0],cost[2])+p[1], min(cost[0],cost[1])+p[2]]
print(min(cost))
