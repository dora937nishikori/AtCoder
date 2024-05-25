def find_non_discarded_cards(n, cards):
    cards = sorted(enumerate(cards), key=lambda x: x[1][0])
    
    non_discarded_indices = []
    min_c_so_far = float('inf')
    
    for i in reversed(range(n)):
        index, (a, c) = cards[i]
        if c < min_c_so_far:
            non_discarded_indices.append(index + 1)  
            min_c_so_far = c
    
    non_discarded_indices.sort()  
    return non_discarded_indices

n = int(input())
cards = []

for _ in range(n):
    A, C = map(int, input().split())
    cards.append((A, C))

non_discarded_cards = find_non_discarded_cards(n, cards)

print(len(non_discarded_cards))
print(*non_discarded_cards)
