def task_1(lines):
    q = 0
    for line in lines:
        line = [*map(int, line.split())]
        diffs = [line[i] - line[i - 1] for i in range(1, len(line))]
        if (
                all(0 < i < 4 for i in diffs) or
                all(-4 < i < 0 for i in diffs)
        ):
            q += 1
    return q


def task_2(lines):
    q = 0
    for line in lines:
        line = [*map(int, line.split())]
        diffs = [line[i] - line[i - 1] for i in range(1, len(line))]
        positive_diffs = list(0 < i < 4 for i in diffs)
        negative_diffs = list(-4 < i < 0 for i in diffs)
        positive_diffs_count = positive_diffs.count(True)
        negative_diffs_count = negative_diffs.count(True)
        if positive_diffs_count > negative_diffs_count:
            use_diffs = positive_diffs
            use_diffs_count = positive_diffs_count
        else:
            use_diffs = negative_diffs
            use_diffs_count = negative_diffs_count
        print(line, use_diffs, use_diffs_count)
        if use_diffs_count == len(line) - 1:
            q += 1
        else:
            line_copy = line.copy()
            line_copy.pop(use_diffs.index(False) + 1)
            print('new use_line', line_copy)
            diffs = [line_copy[i] - line_copy[i - 1] for i in range(1, len(line_copy))]
            if (
                    all(0 < i < 4 for i in diffs) or
                    all(-4 < i < 0 for i in diffs)
            ):
                q += 1
            else:
                # 30 32 33 35 34 35
                line_copy = line.copy()
                line_copy.pop(use_diffs.index(False))
                print('last chance', line_copy)
                diffs = [line_copy[i] - line_copy[i - 1] for i in range(1, len(line_copy))]
                if (
                        all(0 < i < 4 for i in diffs) or
                        all(-4 < i < 0 for i in diffs)
                ):
                    q += 1
    return q


with open('input.txt') as f:
    lines = f.readlines()
    print(task_1(lines))
    print(task_2(lines))
