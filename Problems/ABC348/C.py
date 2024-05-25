n = int(input())
oisisa = {}
for i in range(n):
    a,c = map(int,input().split())
    if c not in oisisa:
        oisisa[c] = a
    elif oisisa[c] > a:
        oisisa[c] = a

oisisa = sorted(oisisa.items(), key=lambda x:x[1], reverse=True)
print(oisisa[0][1])