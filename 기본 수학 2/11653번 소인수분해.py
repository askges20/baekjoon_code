n = int(input())
tmp = n
while True:
    if tmp == 1:
        break
    for i in range(2, tmp+1):
        if tmp % i == 0:
            print(i)
            tmp = tmp//i
            break
