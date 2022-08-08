cards = list(input())

A = '🂡🂱🃁🃑'
c = 100000
p = 0

for _ in range(c):
    random.shuffle(cards)
    for i in range(len(cards) - 3):
        if cards[i] in A and cards[i + 1] in A and cards[i + 2] in A and cards[i + 3] in A:
            p += 1
            break

print(round((p * 100) / c, 2), end='%')
