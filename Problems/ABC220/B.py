K=int(input())
A,B = map(int,input().split())
a=0
b=0
for i,j in enumerate(str(A)[::-1]):
    a += int(j)*K**i
    
for i,j in enumerate(str(B)[::-1]):
    b += int(j)*K**i

print(a*b)