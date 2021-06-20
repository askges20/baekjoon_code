from collections import deque
import sys

tomato=[]
m,n,h=map(int,sys.stdin.readline().split())
tomato=[[sys.stdin.readline().split() for i in range(n)] for j in range(h)]

day=0
dir=[[0,-1,0],[0,1,0],[0,0,-1],[0,0,1],[-1,0,0],[1,0,0]] #좌,우,상,하,앞,뒤
queue=deque([])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]=='1':
                queue.append([i,j,k,0]) #위치, 날짜수

while queue:
    l,x,y,day=queue.popleft()
    for u,v,w in dir:
        next_l,next_x,next_y=l+u,x+v,y+w
        if 0<=next_l<h and 0<=next_x<n and 0<=next_y<m:
            if tomato[next_l][next_x][next_y]=='0': #안익은 토마토
                tomato[next_l][next_x][next_y]='1'
                queue.append([next_l,next_x,next_y,day+1])
                
for t1 in tomato:
    for t2 in t1:
        if '0' in t2: #안익은 토마토가 있을 때
            day=-1
            break
print(day)
