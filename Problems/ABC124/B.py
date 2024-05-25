n=int(input())
h=list(map(int,input().split()))
count = 1
for i in range(1,n):
    if all(h[i] >= h[x] for x in range(i)):
        count += 1

print(count)