n=int(input())
wine=[0, 0]
dp=[0, 0]
wine.append(int(input()))
dp.append(wine[2])
for i in range(3,n+2):
    wine.append(int(input()))
    dp.append(max(dp[i-1],dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i]))
print(dp[n+1])
