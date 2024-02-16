import itertools
import math


def parse_input(input: str) -> list[str]:
    return input.strip().splitlines()


def solution(input: str, *slopes: tuple[int, int]) -> int:
    area = parse_input(input)

    return math.prod(
        sum(
            1
            for x, y in zip(itertools.count(0, right), range(0, len(area), down))
            if area[y][x % len(area[y])] == "#"
        )
        for right, down in slopes
    )


def part1(input: str) -> int:
    return solution(input, (3, 1))


def part2(input: str) -> int:
    return solution(input, (1, 1), (3, 1), (5, 1), (7, 1), (1, 2))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
