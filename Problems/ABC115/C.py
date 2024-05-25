n,k = map(int,input().split())
h = [int(input()) for _ in range(n)]
h.sort(reverse=True)
min_len = 10**9
for i in range(n-k+1):
    sa = h[i] - h[i+k-1]
    if sa < min_len:
        min_len = sa

print(min_len)