a,b,k=map(int,input().split())
ans = set()
count = 1
for i in range(a,b+1):
    if count <= k:
        ans.add(i)
        count += 1
    else:
        break

count_re=1
for i in range(b,a-1,-1):
    if count_re <= k:
        ans.add(i)
        count_re += 1
    else:
        break

print(*sorted(ans))