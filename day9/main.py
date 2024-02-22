import more_itertools


def parse_input(input: str) -> list[int]:
    return list(map(int, input.strip().splitlines()))


def get_invalid_number(nums: list[int], length: int) -> int:
    for *preamble, num in more_itertools.sliding_window(nums, length + 1):
        if not any(i for i in preamble if num - i in preamble):
            return num

    return -1


def part1(input: str, length: int = 25) -> int:
    nums = parse_input(input)

    return get_invalid_number(nums, length)


def part2(input: str, length: int = 25) -> int:
    nums = parse_input(input)

    invalid_number = get_invalid_number(nums, length)

    for preamble in more_itertools.sliding_window(nums, length):
        for i in range(len(preamble)):
            sum = preamble[i]

            for j in range(i + 1, len(preamble)):
                sum += preamble[j]

                if sum == invalid_number:
                    nums_ = preamble[i : j + 1]
                    return max(nums_) + min(nums_)

    return -1


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
