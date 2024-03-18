N = int(input())
A = [list(map(int, input().split())) for l in range(N)]
for low in A:
    ans = []
    for i,j in enumerate(low):
        if j == 1:
            ans.append(i+1)
    print(*ans)