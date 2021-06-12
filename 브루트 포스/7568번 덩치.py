n = int(input())
body = [] #입력값 저장
ranks = [] #순위 저장

for i in range(n):
    inp = input().split()
    body.append((int(inp[0]),int(inp[1])))
    
for i in range(n):
    rank = 1
    for j in range(n):
        if body[i][0]<body[j][0] and body[i][1]<body[j][1]:
            rank += 1
    ranks.append(rank)

print(ranks[0], end="")
for i in range(1,n):
    print(" "+str(ranks[i]),end="")
