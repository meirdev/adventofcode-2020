from .main import part1


INPUT = """
5764801
17807724
"""


def test_part1():
    assert part1(INPUT) == 14897079


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 17673381
