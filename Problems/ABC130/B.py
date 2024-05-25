n,x = map(int,input().split())
l = list(map(int,input().split()))
count = 1
d=0
for i in l:
    d += i
    if d <= x:
        count += 1
    else:
        break

print(count)