n=int(input())
times=list(map(int,input().split()))
times.sort()

cur=0
sum_time=0
for t in times:
    sum_time += cur+t
    cur+=t
print(sum_time)
