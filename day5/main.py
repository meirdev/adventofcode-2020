import itertools


def parse_input(input: str) -> list[str]:
    return input.strip().splitlines()


def get_ids(input: str) -> list[int]:
    binary_spaces = parse_input(input)

    ids = []

    for space in binary_spaces:
        row = space[:7]
        front, back = 0, 127

        for i in row:
            diff = (back - front) // 2 + 1
            if i == "F":
                back -= diff
            else:
                front += diff

        col = space[7:]
        left, right = 0, 7

        for i in col:
            diff = (right - left) // 2 + 1
            if i == "L":
                right -= diff
            else:
                left += diff

        ids.append(front * 8 + left)

    return sorted(ids)


def part1(input: str) -> int:
    return max(get_ids(input))


def part2(input: str) -> int:
    return next(a + 1 for a, b in itertools.pairwise(get_ids(input)) if b - a == 2)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
