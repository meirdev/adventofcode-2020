from .main import part1, part2


INPUT = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""


def test_part1():
    assert part1(INPUT, 5) == 127


def test_part2():
    assert part2(INPUT, 5) == 62


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 1212510616
    assert part2(input) == 171265123
