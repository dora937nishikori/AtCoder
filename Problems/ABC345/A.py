S = input()
if S[0] == '<' and S[-1] == '>' and '=' in S:
    if '<' in S[1:-1] or '>' in S[1:-1]:
        print('No')
    else:
        print('Yes')
else:
    print('No')