def task_1(row):
    res = ''
    sep = chr(100000)
    for i in range(len(row)):
        if i % 2:
            res += str(sep) * int(row[i])
        else:
            res += str(chr(i // 2)) * int(row[i])
    res = res.rstrip(sep)
    for i in range(len(res)):
        try:
            if res[i] == sep:
                res = res[:i] + res[-1] + res[i + 1:-1]
                res = res.rstrip(sep)
        except IndexError:
            break
    result = 0
    for i in range(len(res)):
        result += int(ord(res[i])) * i
    return result


def task_2(row):
    res = ''
    sep_symbol = chr(100000)
    symbols = []
    seps = []
    for i in range(len(row)):
        if i % 2:
            start_index = len(res)
            res += str(sep_symbol) * int(row[i])
            end_index = len(res)
            if start_index < end_index:
                seps.append([start_index, end_index])
        else:
            symbol = chr(i // 2)
            start_index = len(res)
            res += symbol * int(row[i])
            end_index = len(res)
            symbols.append((symbol, start_index, end_index))
    for i, symbol in enumerate(symbols[::-1]):
        for index, sep in enumerate(seps):
            if sep[0] >= symbol[2]:
                break
            len_symbol = symbol[2] - symbol[1]
            if sep[1] - sep[0] >= len_symbol:
                res = res[:sep[0]] + symbol[0] * len_symbol + res[sep[0] + len_symbol:symbol[
                    1]] + sep_symbol * len_symbol + res[symbol[2]:]
                if sep[1] - sep[0] == len_symbol:
                    seps.pop(index)
                else:
                    seps[index][0] += len_symbol
                break

    result = 0
    for i in range(len(res)):
        if res[i] != sep_symbol:
            result += int(ord(res[i])) * i
    return result


with open('input.txt') as f:
    text = f.read()
    print(task_1(text))
    print(task_2(text))
