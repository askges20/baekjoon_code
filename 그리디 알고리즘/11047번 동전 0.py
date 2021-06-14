inp=input().split()
n=int(inp[0])
k=int(inp[1])
digit=[]
for i in range(n):
    digit.append(int(input()))
digit.sort(reverse=True)

sum=0
left=k
for d in digit:
    if left>=d:
        sum += left//d
        left = left%d
        if left==0:
            break
print(sum)
