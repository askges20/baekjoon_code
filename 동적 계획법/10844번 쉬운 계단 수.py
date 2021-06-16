n=int(input())
s=[0,{}]
for i in range(1,10):
    s[1][i]=1

for j in range(2,n+1):
    s.append({})
    for k in range(0,10):
        s[j][k]=0
    
    for num in s[j-1].keys():
        if num==0:
            s[j][1]+=s[j-1][num]
            continue
        if num==9:
            s[j][8]+=s[j-1][num]
            continue
        s[j][num-1]+=s[j-1][num]
        s[j][num+1]+=s[j-1][num]
print(sum(s[n].values())%1000000000)
