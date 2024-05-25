a,b = map(int,input().split())
flag = False
for i in range(1,10000):
    if i*8//100 == a and i//10==b:
        flag = True
        print(i)
        break

if flag == False:
    print(-1)

