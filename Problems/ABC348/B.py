import math
def dist(x1,y1,x2,y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

n = int(input())
zahyou = []
for i in range(n):
    zahyou.append(list(map(int,input().split())))

for i in zahyou:
    max_kyori = 0
    p = 0
    for num,j in enumerate(zahyou):
        kyori = dist(i[0],i[1],j[0],j[1])
        if kyori > max_kyori:
            max_kyori = kyori
            p = num+1
    
    print(p)