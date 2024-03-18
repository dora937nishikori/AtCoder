def count_unique_swaps(s):
    unique_swaps = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):  # iより後ろの文字との組み合わせのみを処理
            if s[i] != s[j]:  # 同じ文字の場合は処理しない
                swapped = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                unique_swaps.add(swapped)
    return len(unique_swaps)

S = input()
print(count_unique_swaps(S))
