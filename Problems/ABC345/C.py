def swap_characters(s, i, j):
    # 文字列をリストに変換して、指定された位置の文字を入れ替える
    s_list = list(s)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    # 入れ替えた文字列を返す
    return ''.join(s_list)

S = input()
change = set()
for i in range(len(S)):
    for j in range(len(S)):
        if i != j:
            change.add(swap_characters(S,i,j))

print(len(change))