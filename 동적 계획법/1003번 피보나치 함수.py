def f(n):
    cnt_0=[1,0]
    cnt_1=[0,1]
    for i in range(2,n+1):
        cnt_0.append(cnt_0[i-2]+cnt_0[i-1])
        cnt_1.append(cnt_1[i-2]+cnt_1[i-1])
    print(cnt_0[n], cnt_1[n])

c=int(input())
for j in range(c):
    n=int(input())
    f(n)
