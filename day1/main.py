import itertools
import math


def parse_input(input: str) -> list[int]:
    return list(map(int, input.strip().splitlines()))


def solution(input: str, nums: int) -> int:
    expenses = parse_input(input)

    return next(
        (
            math.prod(i)
            for i in itertools.product(expenses, repeat=nums)
            if sum(i) == 2020
        ),
        -1,
    )


def part1(input: str) -> int:
    return solution(input, 2)


def part2(input: str) -> int:
    return solution(input, 3)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
