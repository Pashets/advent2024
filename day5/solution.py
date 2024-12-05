from collections import defaultdict


def get_rules_and_checks(lines):
    rules = defaultdict(set)
    checks = []
    is_checks_now = False
    for rule in lines:
        if rule == '':
            is_checks_now = True
            continue
        if is_checks_now:
            checks.append([*map(int, rule.split(','))])
        else:
            rule = [*map(int, rule.split('|'))]
            rules[rule[0]].add(rule[1])
    return rules, checks


def task_1(lines):
    lines = [line.strip() for line in lines]
    rules, checks = get_rules_and_checks(lines)
    # print(rules)
    # print(checks)
    right_checks = []
    for check in checks:
        for i in range(len(check) - 1):
            if set(check[i + 1:]) - rules.get(check[i], set()) != set():
                # print(check, check[i])
                break
        else:
            right_checks.append(check)
    # print(right_checks)
    return sum(right_check[len(right_check) // 2] for right_check in right_checks)


def check_trouble(check, rules):
    for i in range(len(check) - 1):
        if set(check[i + 1:]) - rules.get(check[i], set()) != set():
            return i, set(check[i + 1:]) - rules.get(check[i], set())
    return None, None


def fix_check_trouble(check, index, rules, troubles):
    rule = rules.get(check[index], set())
    if not rule:
        last = check[index]
        check.pop(index)
        check.append(last)
    else:
        # print(rule)
        move_indexes = []
        move_numbers = []
        for i in range(index + 1, len(check)):
            if check[i] in troubles:
                move_indexes.append(i)
                move_numbers.append(check[i])
        for i in sorted(move_indexes, reverse=True):
            check.pop(i)
        check = move_numbers + check
    index, troubles = check_trouble(check, rules)
    if index is not None:
        # print(check, check[index], troubles, 'again')
        return fix_check_trouble(check, index, rules, troubles)
    return check


def task_2(lines):
    lines = [line.strip() for line in lines]
    rules, checks = get_rules_and_checks(lines)
    # print(rules)
    corrected_checks = []
    for check in checks:
        index, troubles = check_trouble(check, rules)
        if index is not None:
            # print(check, check[index], troubles)
            check = fix_check_trouble(check, index, rules, troubles)
            corrected_checks.append(check)
    # print(corrected_checks)
    return sum(corrected_checks[len(corrected_checks) // 2] for corrected_checks in corrected_checks)


with open('input.txt') as f:
    text = f.readlines()
    print(task_1(text))
    print(task_2(text))
