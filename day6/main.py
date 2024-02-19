import itertools
import functools


def parse_input(input: str) -> list[list[str]]:
    return [group.splitlines() for group in input.strip().split("\n\n")]


def part1(input: str) -> int:
    groups = parse_input(input)

    return sum(len(set(itertools.chain.from_iterable(group))) for group in groups)


def part2(input: str) -> int:
    groups = parse_input(input)

    return sum(
        sum(1 for _ in functools.reduce(lambda a, b: a & b, map(set, group)))
        for group in groups
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
