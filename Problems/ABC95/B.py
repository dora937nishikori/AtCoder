n,x = map(int,input().split())
m = [int(input()) for i in range(n)]
for i in m:
    x -= i
count = n
count += x//min(m)
print(count)
