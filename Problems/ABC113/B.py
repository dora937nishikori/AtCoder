n = int(input())
t, a = map(int,input().split())
h = list(map(int,input().split()))
min_kionsa = 1000000
ans = 0
for i in range(n):
    kion = t - h[i]*0.006
    kionsa = abs(a - kion)
    if kionsa < min_kionsa:
        min_kionsa = kionsa
        ans = i + 1
print(ans)

