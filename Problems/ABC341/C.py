H,W,N = map(int,input().split())
T = input()
S = [list(input()) for _ in range(H)]
ans = 0

for i,row in enumerate(S):
    for j,grid in enumerate(row):
        if grid == '#':
            continue
        I = i
        J = j
        is_okay = True
        for word in T:
            if word == 'L':
                J -= 1
            elif word == 'R':
                J += 1
            elif word == 'U':
                I -= 1
            elif word == 'D':
                I += 1        
            if S[I][J] == '#':
                is_okay = False
                break
        
        if is_okay:
            ans += 1

print(ans)