from .main import part1, part2


INPUT = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""


def test_part1():
    assert part1(INPUT) == 37


def test_part2():
    assert part2(INPUT) == 26


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 2113
    assert part2(input) == 1865
