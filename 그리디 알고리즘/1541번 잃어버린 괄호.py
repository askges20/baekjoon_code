exp=input().split('-')
sum=0
for i in range(len(exp)):
    e=exp[i].split('+')
    if i==0:
        for j in range(len(e)):
            sum+=int(e[j])
    else:
        for k in range(len(e)):
            sum-=int(e[k])
print(sum)
