num = int(input()) #테스트 케이스 수
results = []
for i in range(num):
    k = int(input())
    n = int(input())
    apart=[]
    for a in range(k+1):
        apart.append([])
        for b in range(n+1):
            apart[a].append(0)
            
    for j in range(1, n+1): #0층
        apart[0][j] = j
    for a in range(1, k+1): #나머지 층
        for b in range(1, n+1):
            apart[a][b] = apart[a][b] + apart[a-1][b] + apart[a][b-1]
    results.append(int(apart[k][n]))
    
for r in results:
    print(r)
