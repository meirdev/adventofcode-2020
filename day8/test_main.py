from .main import part1, part2


INPUT = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def test_part1():
    assert part1(INPUT) == 5


def test_part2():
    assert part2(INPUT) == 8


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 1563
    assert part2(input) == 767
