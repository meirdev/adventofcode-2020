from .main import part1, part2


INPUT = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


def test_part1():
    assert part1(INPUT) == 220


def test_part2():
    assert part2(INPUT) == 19208


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 3034
    assert part2(input) == 259172170858496
