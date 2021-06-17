n, k=map(int,input().split())
stuff=[[0,0]]
dp=[[0]*(k+1) for _ in range(n+1)]
#dp[a][b] : 1~a번째 물품까지 고려했을 때, 최대 무게가 b인 배낭에 넣을 수 있는 최대 가치

for _ in range(n):
    stuff.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        weight=stuff[i][0] #현재 물품의 무게
        value=stuff[i][1] #현재 물품의 가치
        
        if weight > j: #배낭의 최대 무게보다 물품 무게가 클 경우
            dp[i][j]=dp[i-1][j] #이전 물품까지 고려한 가치 최댓값
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight]+value)
            #이전 물품까지 고려했을때 최대 가치 or 현재 물품으로 대체했을 때 최대 가치 중 큰것

print(dp[n][k])

#너무 어려워...........