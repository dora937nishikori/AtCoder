def remove_between_symbols(text, symbol):
    start_index = text.find(symbol)
    end_index = text.find(symbol, start_index + 1)
    if start_index != -1 and end_index != -1:
        return text[:start_index] + text[end_index + 1:]
    return text

S = input()
symbol = '|'
result = remove_between_symbols(S, symbol)
print(result)