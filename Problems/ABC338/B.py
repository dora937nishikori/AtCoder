S = input()
ans = 'a'
for i in range(ord('b'), ord('z')+1):
    c = chr(i)
    if S.count(c) > S.count(ans):
        ans = c

print(ans)