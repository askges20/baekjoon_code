n=int(input())
nums=[0]+list(map(int,input().split()))
dp=[0]
for i in range(1,n+1):
    dp.append(max(nums[i],dp[i-1]+nums[i]))
print(max(dp[1:]))
