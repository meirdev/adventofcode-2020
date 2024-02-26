from .main import part1, part2


INPUT = """
939
7,13,x,x,59,x,31,19
"""


def test_part1():
    assert part1(INPUT) == 295


def test_part2():
    assert part2(INPUT) == 1068781


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 203
    assert part2(input) == 905694340256752
