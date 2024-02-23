import collections
import functools


def parse_input(input: str) -> list[int]:
    return list(map(int, input.strip().splitlines()))


def part1(input: str) -> int:
    adapters = parse_input(input)

    i, differences = 0, collections.Counter({3: 1})

    for rate in sorted(adapters):
        differences[rate - i] += 1
        i = rate

    return differences[3] * differences[1]


def part2(input: str) -> int:
    adapters = parse_input(input)

    adapters.sort()
    adapters = [0, *adapters, max(adapters) + 3]

    @functools.cache
    def arrangements(adapter) -> int:
        if adapter == 0:
            return 1

        return sum(
            map(
                arrangements,
                filter(lambda i: i in adapters, range(adapter - 3, adapter)),
            )
        )

    return arrangements(adapters[-1])


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
