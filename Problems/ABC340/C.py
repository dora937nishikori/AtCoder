import math
N = int(input())
N_list = [N]
ans = 0
while len(N_list) != 0:
    X = N_list.pop(0)
    x = X/2
    if math.ceil(x) >= 2:
        N_list.append(math.ceil(x))
    if math.floor(x) >= 2:
        N_list.append(math.floor(x))
    ans += X

    
print(ans)