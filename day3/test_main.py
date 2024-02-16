from .main import part1, part2


INPUT = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


def test_part1():
    assert part1(INPUT) == 7


def test_part2():
    assert part2(INPUT) == 336


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 159
    assert part2(input) == 6419669520
