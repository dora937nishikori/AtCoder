h = int(input())
count = 2
se = 0
i = 0
while se < h:
    se += count ** i
    i += 1

if se == h:
    print(i+1)
else:
    print(i)