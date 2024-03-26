N = int(input())
A = int(input())

ans = N % 500
if ans <= A:
    print('Yes')
else:
    print('No')