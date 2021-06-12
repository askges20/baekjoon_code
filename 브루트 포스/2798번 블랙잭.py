m = int((input().split())[1])
cards = list(map(int, input().split()))
maxSum = 0
for a in range(len(cards)-2):
    for b in range(a+1, len(cards)-1):
        for c in range(b+1, len(cards)):
            if cards[a]+cards[b]+cards[c] <= m:
                maxSum = max(maxSum, cards[a]+cards[b]+cards[c])
print(maxSum)
