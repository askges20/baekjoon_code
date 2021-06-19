maze=[]
n,m=map(int,input().split())
for _ in range(n):
    maze.append(list(input()))

queue=[[0,0]]
maze[0][0]=1 #시작점 숫자 1로 초기화
dir=[[-1,0],[1,0],[0,-1],[0,1]] #좌,우,상,하

#BFS
while queue:
    x,y=queue.pop(0)
    for i in range(4):
        next_x,next_y=x+dir[i][0],y+dir[i][1]
        if 0<=next_x<n and 0<=next_y<m and maze[next_x][next_y]=='1': #방문 안한 곳
            queue.append([next_x,next_y])
            maze[next_x][next_y]=maze[x][y]+1
print(maze[n-1][m-1])
