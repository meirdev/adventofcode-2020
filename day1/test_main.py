from .main import part1, part2


INPUT = """
1721
979
366
299
675
1456
"""


def test_part1():
    assert part1(INPUT) == 514579


def test_part2():
    assert part2(INPUT) == 241861950


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 605364
    assert part2(input) == 128397680
