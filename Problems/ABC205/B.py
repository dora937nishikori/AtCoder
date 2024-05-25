n = int(input())
a = list(map(int,input().split()))
ans = [i for i in range(1,n+1)]
a.sort()
if a == ans:
    print('Yes')
else:
    print('No')