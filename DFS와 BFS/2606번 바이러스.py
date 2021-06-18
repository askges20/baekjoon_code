n=int(input()) #컴퓨터 수(노드)
m=int(input()) #연결 수(간선)
edges=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    edge=list(map(int,input().split()))
    edges[edge[0]][edge[1]]=1
    edges[edge[1]][edge[0]]=1

def bfs(node):
    visited=[node]
    queue=[node]
    while queue:
        cur_node=queue.pop(0)
        for next_node in range(n+1):
            if edges[cur_node][next_node]==1 and (next_node not in visited):
                visited.append(next_node)
                queue.append(next_node)
    return visited

print(len(bfs(1))-1)
