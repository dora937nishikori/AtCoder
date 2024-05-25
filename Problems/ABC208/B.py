from math import factorial
P=int(input())
ans = 0
for i in range(10,0,-1):
    while factorial(i) <= P:
        ans += 1
        P -= factorial(i)

print(ans)