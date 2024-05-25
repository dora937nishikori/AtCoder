n = int(input())
data = [list(map(str, input().split())) for _ in range(n)]
data.sort()
sum = 0
for i in data:
    sum += int(i[1])

print(data[sum%n][0])