N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
L = int(input())
C = list(map(int,input().split()))
Q = int(input())
X = list(map(int,input().split()))

S = set()
for a in A:
    for b in B:
        for c in C:
            S.add(a+b+c)

for x in X:
    if x in S:
        print('Yes')
    else:
        print('No')