from .main import part1, part2


INPUT = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""


def test_part1():
    assert part1(INPUT) == 306


def test_part2():
    assert part2(INPUT) == 291


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 33403
    assert part2(input) == 29177
