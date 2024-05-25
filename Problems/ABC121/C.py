n,m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]
A = sorted(A, key = lambda x:x[0])
count = 0
for i in A:
    if m >= i[1]:
        m -= i[1]
        count += i[0]*i[1]
    else:
        count += i[0]*m
        break

print(count)