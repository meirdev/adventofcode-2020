from .main import part1, part2


INPUT = """
F10
N3
F7
R90
F11
"""


def test_part1():
    assert part1(INPUT) == 25


def test_part2():
    assert part2(INPUT) == 286


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 858
    assert part2(input) == 39140
