def task_1(lines):
    size = len(lines)
    for i in range(size):
        lines[i] = lines[i].strip()
    amount = 0
    for l in lines:
        amount += l.count('XMAS') + l.count('SAMX')
    # print(amount)
    t_lines = []
    for i in range(size):
        t_line = ''
        for j in range(len(lines[i])):
            t_line += lines[j][i]
        t_lines.append(t_line)
    # print(t_lines)
    for l in t_lines:
        amount += l.count('XMAS') + l.count('SAMX')
    # print(amount)

    diag_left_lines = []
    for i in range(size - 4, -1, -1):
        d_line = ''
        for j in range(size - i):
            d_line += lines[i + j][j]
        diag_left_lines.append(d_line)
    for j in range(1, len(lines[0]) - 3):
        d_line = ''
        for i in range(size - j):
            d_line += lines[i][j + i]
        diag_left_lines.append(d_line)
    # print(*diag_left_lines, sep='\n')

    for l in diag_left_lines:
        amount += l.count('XMAS') + l.count('SAMX')
    # print(amount)

    diag_right_lines = []
    for j in range(3, len(lines[0])):
        d_line = ''
        for i in range(j + 1):
            d_line += lines[i][j - i]
        diag_right_lines.append(d_line)
    for i in range(1, size - 3):
        d_line = ''
        for j in range(size - i):
            d_line += lines[size - j - 1][i + j]
        diag_right_lines.append(d_line)
    # print(*diag_right_lines, sep='\n')
    for l in diag_right_lines:
        amount += l.count('XMAS') + l.count('SAMX')
    return amount


def task_2(lines):
    amount = 0
    size = len(lines)
    all_A_coords = []
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            if lines[i][j] == 'A':
                all_A_coords.append((i, j))
    print(all_A_coords)
    for coord in all_A_coords:
        lt = lines[coord[0] - 1][coord[1] - 1]
        rt = lines[coord[0] - 1][coord[1] + 1]
        rb = lines[coord[0] + 1][coord[1] + 1]
        lb = lines[coord[0] + 1][coord[1] - 1]
        if sorted(lt + rb) == ['M', 'S'] and sorted(rt + lb) == ['M', 'S']:
            amount += 1

    return amount


with open('input.txt') as f:
    text = f.readlines()
    print(task_1(text))
    print(task_2(text))
