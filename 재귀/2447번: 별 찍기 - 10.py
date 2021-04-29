def star(n):
    if n==3:
        return ["***","* *","***"]
    else:
        old = star(n//3)
        new = []
        for j in range(n):
            new.append('')
            
        for a in range(n//3):
            new[a]=old[a]*3
            new[n-a-1]=old[a]*3
            
        for b in range(n//3, n//3*2):
            new[b]=old[b-n//3] + ' '*(n//3) + old[b-n//3]
            
        return new
        

n = int(input())
star = star(n)
for i in range(n):
    print(star[i])
