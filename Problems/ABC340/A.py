A, B, D = map(int,input().split())
ans = [A]
add = A
while add != B:
    add += D
    ans.append(add)
    if add == B:
        break

print(*ans)