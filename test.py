s = input()
t = input()
ans = []
ok = []
for i,t_word in enumerate(t):
    for s_word in s:
        if s_word in ok:
            continue
        if t_word == s_word:
            ans.append(i + 1)
            ok.append(s_word)
            break

print(*ans)
