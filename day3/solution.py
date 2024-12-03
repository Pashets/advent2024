import re


def task_1(text):
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', text)
    return sum(int(m1) * int(m2) for m1, m2 in matches)


def task_2(text):
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))', text)
    enable_matches = []
    enable_futures = True
    for match in matches:
        if "don't()" in match:
            enable_futures = False
        elif 'do()' in match:
            enable_futures = True
        else:
            if enable_futures:
                enable_matches.append((match[0], match[1]))
    return sum(int(m1) * int(m2) for m1, m2 in enable_matches)


with open('input.txt') as f:
    text = f.read()
    print(task_1(text))
    print(task_2(text))
