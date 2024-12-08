from copy import deepcopy


def task_1(lines):
    lines = [l.strip() for l in lines]
    size = len(lines)
    t_lines = []
    for i in range(size):
        t_lines_row = ''
        for j in range(size):
            t_lines_row += lines[j][i]
            if lines[i][j] == '^':
                position = (i, j)
        t_lines.append(t_lines_row)
    direction = 'top'
    path = [position]
    while True:
        x, y = position
        if direction == 'top':
            obstacle = t_lines[position[1]].rfind('#', 0, x)
            if obstacle == -1:
                path += [(i, y) for i in range(x - 1, -1, -1)]
                break
            path += [(i, y) for i in range(x - 1, obstacle, -1)]
            direction = 'right'
        elif direction == 'right':
            obstacle = lines[position[0]].find('#', y)
            if obstacle == -1:
                path += [(x, i) for i in range(y + 1, size)]
                break
            path += [(x, i) for i in range(y + 1, obstacle)]
            direction = 'bottom'
        elif direction == 'bottom':
            obstacle = t_lines[position[1]].find('#', x)
            if obstacle == -1:
                path += [(i, y) for i in range(x + 1, size)]
                break
            path += [(i, y) for i in range(x + 1, obstacle)]
            direction = 'left'
        elif direction == 'left':
            obstacle = lines[position[0]].rfind('#', 0, y)
            if obstacle == -1:
                path += [(x, i) for i in range(y - 1, -1, -1)]
                break
            path += [(x, i) for i in range(y - 1, obstacle, -1)]
            direction = 'top'
        position = path[-1]

    print(path)
    print(len(path))
    print(set(path))
    return len(set(path))


def find_path_or_cycle(lines):
    size = len(lines)
    t_lines = []
    for i in range(size):
        t_lines_row = ''
        for j in range(size):
            t_lines_row += lines[j][i]
            if lines[i][j] == '^':
                position = (i, j)
        t_lines.append(t_lines_row)
    direction = 'top'
    path = [position]
    path_parts = set()
    while True:
        x, y = position
        if direction == 'top':
            obstacle = t_lines[position[1]].rfind('#', 0, x)
            if obstacle == -1:
                path += [(i, y) for i in range(x - 1, -1, -1)]
                break
            path_part = [(i, y) for i in range(x - 1, obstacle, -1)]
            direction = 'right'
        elif direction == 'right':
            obstacle = lines[position[0]].find('#', y)
            if obstacle == -1:
                path += [(x, i) for i in range(y + 1, size)]
                break
            path_part = [(x, i) for i in range(y + 1, obstacle)]
            direction = 'bottom'
        elif direction == 'bottom':
            obstacle = t_lines[position[1]].find('#', x)
            if obstacle == -1:
                path += [(i, y) for i in range(x + 1, size)]
                break
            path_part = [(i, y) for i in range(x + 1, obstacle)]
            direction = 'left'
        elif direction == 'left':
            obstacle = lines[position[0]].rfind('#', 0, y)
            if obstacle == -1:
                path += [(x, i) for i in range(y - 1, -1, -1)]
                break
            path_part = [(x, i) for i in range(y - 1, obstacle, -1)]
            direction = 'top'
        path_part_tuple = tuple(sorted(path_part)) + (direction,)
        if path_part_tuple in path_parts:
            return "CYCLE"
        if path_part:
            path_parts.add(path_part_tuple)
        path += path_part
        position = path[-1]
    return path


def task_2(lines):
    lines = [l.strip() for l in lines]
    size = len(lines)
    amount = 0
    for i in range(size):
        for j in range(size):
            if lines[i][j] == '^':
                continue
            new_lines = deepcopy(lines)
            new_lines[i] = new_lines[i][:j] + '#' + new_lines[i][j + 1:]
            path = find_path_or_cycle(new_lines)
            if path == "CYCLE":
                amount += 1
                print(amount)
    return amount


with open('input.txt') as f:
    text = f.readlines()
    print(task_1(text))
    print(task_2(text))
