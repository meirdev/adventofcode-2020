from .main import part1, part2


INPUT_PART_1 = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

INPUT_PART_2 = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""


def test_part1():
    assert part1(INPUT_PART_1) == 165


def test_part2():
    assert part2(INPUT_PART_2) == 208


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 10452688630537
    assert part2(input) == 2881082759597
