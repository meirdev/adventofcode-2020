from .main import part1, part2


INPUT_PART_1 = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

INPUT_PART_2 = """
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""


def test_part1():
    assert part1(INPUT_PART_1) == 71


def test_part2():
    assert part2(INPUT_PART_2, "") == 11 * 12 * 13


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 26941
    assert part2(input) == 634796407951
