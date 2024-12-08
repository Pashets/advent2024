from collections import defaultdict
from functools import reduce


def is_correct(result, numbers):
    max_possible = reduce(lambda x, y: x * y, numbers)
    if max_possible == result:
        return True
    count_operators = (len(numbers) - 1)
    for i in range(2 ** count_operators):
        local_result = numbers[0]
        for index, j in enumerate(bin(i)[2:].zfill(count_operators)):
            if j == '0':
                local_result += numbers[index + 1]
            elif j == '1':
                local_result *= numbers[index + 1]
        if local_result == result:
            return True


def task_1(lines):
    rows = defaultdict(list)
    for line in lines:
        res, numbers = line.split(':')
        rows[int(res)].append(list(map(int, numbers.split())))
    amount = 0
    for res, list_numbers in rows.items():
        for numbers in list_numbers:
            if is_correct(res, numbers):
                amount += res
    return amount


def to_ternary(n: int) -> str:
    if n == 0:
        return "0"
    ternary = ""
    while n > 0:
        ternary = str(n % 3) + ternary
        n //= 3

    return ternary


def is_correct_2(result, numbers):
    max_possible = reduce(lambda x, y: x * y, numbers)
    if max_possible == result:
        return True
    count_operators = (len(numbers) - 1)
    for i in range(3 ** count_operators):
        local_result = numbers[0]
        for index, j in enumerate(to_ternary(i).zfill(count_operators)):
            if j == '0':
                local_result += numbers[index + 1]
            elif j == '1':
                local_result *= numbers[index + 1]
            elif j == '2':
                local_result = int(str(local_result) + str(numbers[index + 1]))
        if local_result == result:
            return True


def task_2(lines):
    rows = defaultdict(list)
    for line in lines:
        res, numbers = line.split(':')
        rows[int(res)].append(list(map(int, numbers.split())))
    amount = 0
    for res, list_numbers in rows.items():
        for numbers in list_numbers:
            if is_correct_2(res, numbers):
                amount += res
    return amount


with open('input.txt') as f:
    text = f.readlines()
    print(task_1(text))
    print(task_2(text))
