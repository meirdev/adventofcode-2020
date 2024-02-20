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


@functools.cache
def solution(input: str) -> dict[str, Counter[str]]:
    bag2bags = parse_input(input)

    @functools.cache
    def inner(bag: str, n: int) -> Counter[str]:
        bags = collections.Counter({bag: n})
        for bag_, n_ in bag2bags[bag].items():
            bags.update(inner(bag_, n_ * n))
        return bags

    bags_counter: dict[str, Counter[str]] = {}

    for bag in bag2bags:
        bags: Counter[str] = collections.Counter()
        bags.update(inner(bag, 1))
        bags_counter[bag] = bags

    return bags_counter


def part1(input: str) -> int:
    bags_counter = solution(input)

    return sum(1 for bags in bags_counter.values() if SHINY_GOLD in bags) - 1


def part2(input: str) -> int:
    bags_counter = solution(input)

    return bags_counter[SHINY_GOLD].total() - 1


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
