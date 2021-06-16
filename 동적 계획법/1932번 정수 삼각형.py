n=int(input())
cost=[]
cost.append(int(input()))
for i in range(2,n+1):
    inp=list(map(int,input().split()))
    tmp=[cost[0]+inp[0]]
    for j in range(1,i-1):
            tmp.append(max(cost[j-1],cost[j])+inp[j])
    tmp.append(cost[i-2]+inp[i-1])
    cost=tmp
print(max(cost))
