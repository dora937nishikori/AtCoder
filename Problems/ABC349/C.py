S = list(input())
T = list(input().lower())
if T[-1] == 'x':
    T = T[:-1]

def is_subsequence(T, S):
    t_index = 0
    for s in S:
        if t_index < len(T) and T[t_index] == s:
            t_index += 1
    return t_index == len(T)

if is_subsequence(T,S):
    print('Yes')
else:
    print('No')
