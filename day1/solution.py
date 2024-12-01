def task_1(lines):
    left_side = []
    right_side = []
    for line in lines:
        l, r = map(int, line.split())
        left_side.append(l)
        right_side.append(r)
    left_side.sort()
    right_side.sort()
    return sum(abs(l - r) for l, r in zip(left_side, right_side))


def task_2(lines):
    left_side = []
    right_side = []
    for line in lines:
        l, r = map(int, line.split())
        left_side.append(l)
        right_side.append(r)
    set_left_side = set(left_side)
    return sum(l * left_side.count(l) * right_side.count(l) for l in set_left_side)


with open('input.txt') as f:
    lines = f.readlines()
    print(task_1(lines))
    print(task_2(lines))
