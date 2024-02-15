from .main import part1, part2


INPUT = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


def test_part1():
    assert part1(INPUT) == 2


def test_part2():
    assert part2(INPUT) == 1


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 515
    assert part2(input) == 711
