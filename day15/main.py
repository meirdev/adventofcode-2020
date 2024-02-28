import collections
from typing import DefaultDict, Deque


def parse_input(input: str) -> list[int]:
    return list(map(int, input.split(",")))


def solution(input: str, th: int) -> int:
    numbers = parse_input(input)

    index: DefaultDict[int, Deque[int]] = collections.defaultdict(
        lambda: collections.deque(maxlen=2)
    )

    for i, number in enumerate(numbers):
        index[number].appendleft(i)

    last_spoken = numbers[-1]

    for i in range(len(numbers), th):
        if len(index[last_spoken]) < 2:
            last_spoken = 0
        else:
            last_spoken = index[last_spoken][0] - index[last_spoken][1]
        index[last_spoken].appendleft(i)

    return last_spoken


def part1(input: str) -> int:
    return solution(input, 2020)


def part2(input: str) -> int:
    return solution(input, 30000000)


def main() -> None:
    input = "2,0,1,7,4,14,18"

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
