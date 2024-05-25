n = int(input())
d = list(map(int,input().split()))
d.sort()
x = n//2
print(d[x]-d[x-1])