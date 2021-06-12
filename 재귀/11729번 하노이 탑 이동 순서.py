def hanoi(n, f, tmp, to):
    if n==1:
        print(f, to)
    else:
        hanoi(n-1, f, to, tmp)
        print(f, to)
        hanoi(n-1, tmp, f, to)

n = int(input())
print(pow(2,n)-1)
hanoi(n, 1, 2, 3)
