# 空のリストを作成して、入力された整数を格納する
numbers = []

# ユーザーが入力を終了するまでループを続ける
while True:
    try:
        # 一行分の入力を取得
        line = int(input())
        
        numbers.append(line)

        if line == 0:
            break
    except ValueError:
        print()

for i in reversed(numbers):
    print(i)

