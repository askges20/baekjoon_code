n=int(input())
arr=list(map(int,input().split()))
LIS=[1]*n
LDS=[1]*n
for i in range(n):
    for j in range(i):
        if arr[j]<arr[i]:
            LIS[i]=max(LIS[i],LIS[j]+1)
for a in range(n-1,-1,-1):
    for b in range(n-1,a-1,-1):
        if arr[b]<arr[a]:
            LDS[a]=max(LDS[a],LDS[b]+1)
max_len=0
for c in range(n):
    max_len=max(max_len,LIS[c]+LDS[c])
print(max_len-1)
