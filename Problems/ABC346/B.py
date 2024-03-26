def check_substring(x, y):
    S = 'wbwbwwbwbwbw' * (max(x, y) // 6 + 1)  # 文字列Sを十分に長くする
    n = len(S)
    w_count = 0
    b_count = 0

    # Sをx個の'w'とy個の'b'からなる部分文字列で探す
    for i in range(n):
        if S[i] == 'w':
            w_count += 1
        else:
            b_count += 1

        # 現在の部分文字列が条件を満たすかどうかを確認
        if w_count == x and b_count == y:
            return True

        # 条件を満たす部分文字列が見つからない場合、w_countとb_countをリセット
        if w_count > x or b_count > y:
            w_count = 0
            b_count = 0

    return False

x,y = map(int,input().split())
if check_substring(x,y):
    print('Yes')
else:
    print('No')
