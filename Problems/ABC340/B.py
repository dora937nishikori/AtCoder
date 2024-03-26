Q = int(input())
query = [list(map(int,input().split())) for _ in range(Q)]
A = []
for i in range(Q):
    if query[i][0] == 1:
        A.append(query[i][1])
    else:
        print(A[-query[i][1]])