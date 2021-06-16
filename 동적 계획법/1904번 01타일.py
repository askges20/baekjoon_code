r=[0,1,2]
n=int(input())
for i in range(3,n+1):
    r.append((r[i-2]+r[i-1])%15746)
print(r[n]%15746)

#피보나치 수열인것은 파악했으나 append할 때 %15746을 안해서 메모리 초과 났었음,,