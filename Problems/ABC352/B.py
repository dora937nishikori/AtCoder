s = input()
t = input()
ans = []
ok = []
for i in range(len(t)):
    for j in range(len(s)):
        if s[j] in ok:
            continue
        if t[i] == s[j]:
            ans.append(i+1)
            ok.append(s[j])
            break

print(*ans)