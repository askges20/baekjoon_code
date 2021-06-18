n=int(input())
apart=[]
for _ in range(n):
    apart.append(list(map(int,list(input()))))
    
dir=[[-1,0],[1,0],[0,-1],[0,1]] #좌,우,상,하
def dfs(x,y,cnt):
    apart[x][y]=0 #탐색 완료한 아파트 1->0
    for i in range(len(dir)):
        next_x, next_y = x+dir[i][0], y+dir[i][1]
        #범위를 벗어나지 않는 위치 & 아파트가 존재할 때 dfs 실행
        if next_x<0 or next_x>=n or next_y<0 or next_y>=n or not apart[next_x][next_y]:
            continue
        cnt = dfs(next_x, next_y, cnt+1)
    return cnt

estate=[]
for i in range(n):
    for j in range(n):
        if apart[i][j]==1:
            estate.append(dfs(i,j,1))
print(len(estate))
for e in sorted(estate): #오름차순 출력
    print(e)
