dic={}

def w(a,b,c):
    if (str(a)+","+str(b)+","+str(c)) in dic.keys():
        return dic[str(a)+","+str(b)+","+str(c)]
    if a<=0 or b<=0 or c<=0:
        dic[str(a)+","+str(b)+","+str(c)]=1
        return 1
    if a>20 or b>20 or c>20:
        dic[str(a)+","+str(b)+","+str(c)]=w(20,20,20)
        return w(20,20,20)
    if a<b and b<c:
        dic[str(a)+","+str(b)+","+str(c)]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
        return w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
    else:
        dic[str(a)+","+str(b)+","+str(c)]=w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        return w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    
while True:
    inp=list(map(int,input().split()))
    if inp.count(-1)==3:
        break
    print("w(%d, %d, %d) = %d"%(inp[0],inp[1],inp[2],w(inp[0],inp[1],inp[2])))
