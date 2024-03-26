def missing_sum(N, A, K):
    # Aの要素をビットマスクで表現した配列を作成する
    bitmask = 0
    for num in A:
        bitmask |= 1 << (num - 1)  # numをビットマスクにマークする

    total = 0
    # 1からKまでの整数に対してループ
    for i in range(1, K + 1):
        if not (bitmask & (1 << (i - 1))):  # iがビットマスクに含まれていない場合
            total += i

    return total

# 入力を受け取る
N,K = map(int,input().split())
A = list(map(int, input().split()))

# 結果を出力
print(missing_sum(N, A, K))


