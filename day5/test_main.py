from .main import part1, part2


INPUT = """
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""


def test_part1():
    assert part1(INPUT) == 820


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 892
    assert part2(input) == 625
