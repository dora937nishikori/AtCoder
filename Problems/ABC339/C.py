N = int(input())
A = list(map(int,input().split()))
ans = 0
for i in A:
    ans = max(ans+i,0)
print(ans)