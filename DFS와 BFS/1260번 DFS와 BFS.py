n,m,start=map(int,input().split()) #n:노드 개수, m:간선 개수, start:시작 노드
edges=[[0]*(n+1) for _ in range(n+1)] #노드간의 연결을 행렬로 나타냄
for i in range(m):
    edge=list(map(int,input().split()))
    edges[edge[0]][edge[1]]=1
    edges[edge[1]][edge[0]]=1

def bfs(node):
    visited=[node] #방문한 노드 순서
    queue=[node] #탐색할 노드
    while queue: #모든 노드를 탐색할 때까지
        cur_node=queue.pop(0) #현재 탐색 노드
        for next_node in range(n+1):
            #연결되어 있고 방문하지 않은 노드인 경우
            if edges[cur_node][next_node]==1 and (next_node not in visited):
                visited.append(next_node)
                queue.append(next_node)
    return visited

def dfs(node, visited):
    visited.append(node)
    for next_node in range(n+1):
        if edges[node][next_node]==1 and (next_node not in visited):
            dfs(next_node, visited) #재귀 호출
    return visited

print(*dfs(start,[]))
print(*bfs(start))
