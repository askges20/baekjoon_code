n=int(input())
nums=[]
for i in range(n):
    nums.append(list(map(int,input().split())))
nums.sort() #앞의 수로 정렬
arr=[]
for i in range(n):
    arr.append(nums[i][1])

LIS_front=[1]*n
LIS_back=[1]*n
for j in range(n):
    for k in range(j):
        if arr[k]<arr[j]:
            LIS_front[j]=max(LIS_front[j],LIS_front[k]+1)
for a in range(n-1,-1,-1):
    for b in range(n-1,a-1,-1):
        if arr[b]>arr[a]:
            LIS_back[a]=max(LIS_back[a],LIS_back[b]+1)
            
max_len=0
for c in range(n):
    max_len=max(max_len,LIS_front[c]+LIS_back[c])
print(n-max_len+1)
