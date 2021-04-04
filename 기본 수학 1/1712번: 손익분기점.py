inp = input().split()
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])
if b>=c:
    print(-1)
else:
    print(a//(c-b) + 1)
