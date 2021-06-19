#DFS

import sys
sys.setrecursionlimit(1000000)

farm=[] #밭 (배추 위치)
dir=[[-1,0],[1,0],[0,-1],[0,1]] #좌,우,상,하

def dfs(x,y):
    farm[x][y]=0 #배추 발견 1->0 표시
    for i in range(len(dir)):
        next_x,next_y=x+dir[i][0],y+dir[i][1]
        if next_x<0 or next_x>=m or next_y<0 or next_y>=n or not farm[next_x][next_y]:
            continue
        dfs(next_x,next_y) #근처에 있는 배추
    
t=int(input())
for _ in range(t):
    m,n,k=map(int,input().split())
    farm=[[0]*n for _ in range(m)]
    
    for _ in range(k):
        a,b=map(int,input().split())
        farm[a][b]=1 #배추 위치 표시

    cnt=0
    for a in range(m):
        for b in range(n):
            if farm[a][b]==1: #배추 발견
                cnt+=1
                dfs(a,b)
                
    print(cnt)

#RecursionError : 최대 재귀 깊이 기본 1000으로 되어있음
#sys.setrecursionlimit() 이용해서 1000000으로 늘렸음
