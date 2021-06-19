from collections import deque

tomato=[]
m,n=map(int,input().split())
for _ in range(n):
    tomato.append(input().split())

dir=[[-1,0],[1,0],[0,-1],[0,1]] #좌,우,상,하
queue=deque([])

for i in range(n):
    for j in range(m):
        if tomato[i][j]=='1':
            queue.append([i,j,0]) #위치, 날짜수

while queue:
    x,y,day=queue.popleft()
    for j in range(4):
        next_x,next_y=x+dir[j][0],y+dir[j][1]
        if 0<=next_x<n and 0<=next_y<m:
            if tomato[next_x][next_y]=='0': #안익은 토마토
                tomato[next_x][next_y]='1'
                queue.append([next_x,next_y,day+1])
for t in tomato:
    if '0' in t: #안익은 토마토가 있을 때
        day=-1
        break
print(day)
