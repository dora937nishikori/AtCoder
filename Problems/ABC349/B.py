def is_two_of_each_value(dictionary):
    # 辞書の値を集計するための空の辞書を作成
    value_counts = {}
    
    # 与えられた辞書の各値を数える
    for value in dictionary.values():
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1
    
    # 値の数がすべて2つかどうかをチェックする
    unique_counts = set(value_counts.values())
    
    # 2つの値が全ての値の数にあるかどうかを返す
    return len(unique_counts) == 1 and 2 in unique_counts

def create_dictionary_from_string(S):
    # 文字列から辞書を作成する
    char_count = {}
    for char in S:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# テスト用の文字列
test_string = input()

# 文字列から辞書を作成
test_dict = create_dictionary_from_string(test_string)

# 関数の実行と結果の表示
if is_two_of_each_value(test_dict):
    print('Yes')
else:
    print('No')
