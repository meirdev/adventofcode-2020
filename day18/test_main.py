from .main import part1, part2


INPUT = """
1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
"""


def test_part1():
    assert part1(INPUT) == 71 + 51 + 26 + 437 + 12240 + 13632


def test_part2():
    assert part2(INPUT) == 231 + 51 + 46 + 1445 + 669060 + 23340


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 45283905029161
    assert part2(input) == 216975281211165
