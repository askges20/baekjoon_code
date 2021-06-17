s1='_'+input()
s2='_'+input()
m=len(s1)-1 #s1 길이
n=len(s2)-1 #s2 길이
dp=[[0]*(n+1)]
for i in range(1,m+1):
    dp.append([0])
    for j in range(1,n+1):
        if s1[i]==s2[j]:
            dp[i].append(dp[i-1][j-1]+1)
        else:
            dp[i].append(max(dp[i][j-1],dp[i-1][j]))
print(dp[m][n])
