n=int(input())
dis=list(map(int,input().split()))
price=list(map(int,input().split()))

price_sum=price[0]*dis[0]
cur_price=price[0]
for i in range(1,n-1):
    if cur_price>=price[i]:
        cur_price=price[i]
    price_sum+=cur_price*dis[i]
print(price_sum)
