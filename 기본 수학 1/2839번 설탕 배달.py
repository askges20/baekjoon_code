n = int(input())
cnt3 = 0
cnt5 = 0
answer = 0

cnt3 = n//3
tmpN = n%3

while True:
    tmpN = tmpN + 3
    
    if tmpN > n:
        answer = cnt3 + cnt5
        break
    
    if tmpN%5 == 0:
        cnt3 = (n-5*(tmpN//5))//3
        cnt5 = tmpN//5

if 3*cnt3 + 5*cnt5 != n:
    answer = -1
print(answer)
