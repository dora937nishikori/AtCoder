N=int(input())
ans = 0
max_count = 0
for i in range(1,N+1):
    j=i
    count = 0
    while j % 2 == 0:
        count += 1
        j /= 2
    
    if max_count <= count:
        max_count=count
        ans = i

print(ans)