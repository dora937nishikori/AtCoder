X=int(input())
year = 0
count = 100
while count < X:
    risi = int(count//100)
    count += risi
    year += 1

print(year)