from .main import part1, part2


INPUT = "389125467"


def test_part1():
    assert part1(INPUT) == 67384529


def test_part2():
    assert part2(INPUT) == 149245887792


def test_input():
    input = "789465123"

    assert part1(input) == 98752463
    assert part2(input) == 2000455861
