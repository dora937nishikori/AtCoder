n = int(input())
dic = {}
for i in range(n):
    s,t = map(str,input().split())
    dic[s] = int(t)

dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print(dic[1][0])