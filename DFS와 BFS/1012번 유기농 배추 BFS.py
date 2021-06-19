#BFS

farm=[] #밭 (배추 위치)
dir=[[-1,0],[1,0],[0,-1],[0,1]] #좌,우,상,하

def bfs(x,y):
    visited=[[x,y]]
    queue=[[x,y]]
    while len(queue)>0:
        cur=queue.pop(0)
        farm[cur[0]][cur[1]]=0 #배추 발견 1->0
        for i in range(len(dir)):
            next_x,next_y=cur[0]+dir[i][0],cur[1]+dir[i][1]
            if next_x<0 or next_x>=m or next_y<0 or next_y>=n: #범위 벗어나면
                continue
            if farm[next_x][next_y]==0 or [next_x,next_y] in visited:
                continue
            visited.append([next_x,next_y])
            queue.append([next_x,next_y])
    
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
                bfs(a,b)
                
    print(cnt)

#visited를 사용해야 중복 탐색을 방지해서 시간 초과가 나지 않는다.