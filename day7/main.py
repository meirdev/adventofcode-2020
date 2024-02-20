import collections
import functools
import re
from typing import Counter


SHINY_GOLD = "shiny gold"


def parse_input(input: str) -> dict[str, dict[str, int]]:
    bag2bags: dict[str, dict[str, int]] = {}

    for line in input.strip().splitlines():
        first, second = re.split(r"\s+bags contain\s+", line)

        bag2bags[first] = {}

        for bags, color in re.findall(r"(\d+) (.+?) bag", second):
            bag2bags[first][color] = int(bags)

    return bag2bags


def part1(input: str) -> int:
    bag2bags = parse_input(input)

    @functools.cache
    def inner(bag: str) -> set[str]:
        bags = set([bag])
        for bag_ in bag2bags[bag]:
            bags |= inner(bag_)
        return bags

    return sum(1 for bag in bag2bags if bag != SHINY_GOLD and SHINY_GOLD in inner(bag))


def part2(input: str) -> int:
    bag2bags = parse_input(input)

    @functools.cache
    def inner(bag: str, n: int) -> Counter[str]:
        bags = collections.Counter({bag: n})
        for bag_, n_ in bag2bags[bag].items():
            bags.update(inner(bag_, n_ * n))
        return bags

    bags: Counter[str] = collections.Counter()

    for bag, n in bag2bags[SHINY_GOLD].items():
        bags.update(inner(bag, n))

    return bags.total()


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
