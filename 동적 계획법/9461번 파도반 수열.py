p=[0,1,1,1,2,2]
c=int(input())
for i in range(c):
    n=int(input())
    if n<len(p):
        print(p[n])
    else:
        for j in range(len(p),n+1):
            p.append(p[j-5]+p[j-1])
        print(p[n])
