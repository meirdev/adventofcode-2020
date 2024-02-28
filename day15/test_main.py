from .main import part1, part2


INPUT = (
    ("0,3,6", 436, 175594),
    ("1,3,2", 1, 2578),
    ("2,1,3", 10, 3544142),
    ("1,2,3", 27, 261214),
    ("2,3,1", 78, 6895259),
    ("3,2,1", 438, 18),
    ("3,1,2", 1836, 362),
)


def test_part1():
    for input, expected, _ in INPUT:
        assert part1(input) == expected


def test_part2():
    for input, _, expected in INPUT:
        assert part2(input) == expected


def test_input():
    input = "2,0,1,7,4,14,18"

    assert part1(input) == 496
    assert part2(input) == 883
