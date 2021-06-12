n=int(input())
times=[tuple(map(int,input().split())) for _ in range(n)]
times.sort() #회의 시작 시간 기준 정렬
times.sort(key=lambda x:x[1]) #회의 끝 시간 기준 정렬

cur=0 #가장 최근에 한 회의 끝 시간
cnt=0
for t in times:
    if cur<=t[0]: #가장 최근 회의 이후에 시작할 때
        cnt += 1
        cur=t[1]
print(cnt)
