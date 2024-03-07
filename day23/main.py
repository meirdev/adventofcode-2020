import collections
import itertools


def parse_input(input: str) -> list[int]:
    return list(map(int, input))


def part1(input: str) -> int:
    labels = parse_input(input)

    cups, max_value = collections.deque(labels), max(labels)

    for _ in range(100):
        current = cups[0]

        cups.rotate(-1)

        three_cups = (cups.popleft(), cups.popleft(), cups.popleft())

        destination = next(
            cups.index(i)
            for i in itertools.chain(range(current - 1, 0, -1), range(max_value, 0, -1))
            if i not in three_cups
        )

        cups.rotate(-destination - 1)

        cups.extendleft(reversed(three_cups))

        cups.rotate(destination + 1)

    cups_, i = list(cups), cups.index(1)

    return int("".join(map(str, cups_[i + 1 :] + cups_[:i])))


def part2(input: str) -> int:
    cups = parse_input(input)

    cups.extend(range(10, 1_000_001))

    moves = 10_000_000

    max_value = 1_000_000

    labels = [0 for _ in range(len(cups) + 1)]

    for a, b in zip(cups, cups[1:] + cups[:1]):
        labels[a] = b

    current = cups[0]

    for _ in range(moves):
        value = current
        next1 = labels[current]
        next2 = labels[next1]
        next3 = labels[next2]

        while True:
            value -= 1

            if value == 0:
                value = max_value

            if value not in (next1, next2, next3):
                break

        labels[current] = labels[next3]
        labels[next3] = labels[value]
        labels[value] = next1

        current = labels[current]

    return labels[1] * labels[labels[1]]


def main() -> None:
    input = "789465123"

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
