from collections import defaultdict


def task_1(lines):
    lines = [l.strip() for l in lines]
    antennas = defaultdict(list)
    height = len(lines)
    width = len(lines[0])
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '.':
                antennas[lines[i][j]].append((i, j))
    antinodes = []
    for antenna, coords in antennas.items():
        for i in range(len(coords) - 1):
            for j in range(i + 1, len(coords)):
                diff = (coords[j][0] - coords[i][0], coords[j][1] - coords[i][1])
                before_first = (coords[i][0] - diff[0], coords[i][1] - diff[1])
                after_second = (coords[j][0] + diff[0], coords[j][1] + diff[1])
                if 0 <= before_first[0] < height and 0 <= before_first[1] < width:
                    antinodes.append(before_first)
                if 0 <= after_second[0] < height and 0 <= after_second[1] < width:
                    antinodes.append(after_second)
    return len(set(antinodes))


def task_2(lines):
    lines = [l.strip() for l in lines]
    antennas = defaultdict(list)
    height = len(lines)
    width = len(lines[0])
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '.':
                antennas[lines[i][j]].append((i, j))
    antinodes = []
    for antenna, coords in antennas.items():
        for i in range(len(coords) - 1):
            for j in range(i + 1, len(coords)):
                diff = (coords[j][0] - coords[i][0], coords[j][1] - coords[i][1])
                last_before_first = coords[i]
                while True:
                    before_first = (last_before_first[0] - diff[0], last_before_first[1] - diff[1])
                    if 0 <= before_first[0] < height and 0 <= before_first[1] < width:
                        antinodes.append(before_first)
                        last_before_first = before_first
                    else:
                        break
                last_after_second = coords[j]
                while True:
                    after_second = (last_after_second[0] + diff[0], last_after_second[1] + diff[1])
                    if 0 <= after_second[0] < height and 0 <= after_second[1] < width:
                        antinodes.append(after_second)
                        last_after_second = after_second
                    else:
                        break
    for antenna, coords in antennas.items():
        antinodes.extend(coords)
    return len(set(antinodes))


with open('input.txt') as f:
    text = f.readlines()
    print(task_1(text))
    print(task_2(text))
