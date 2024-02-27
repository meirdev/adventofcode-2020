import collections
import itertools
from typing import NamedTuple

SIZE = 2**36


class Init(NamedTuple):
    mask: str
    address: int
    value: int


def parse_input(input: str) -> list[Init]:
    program: list[Init] = []

    mask = ""

    for line in input.strip().splitlines():
        type, value = line.split(" = ")

        if type == "mask":
            mask = value
        else:
            index = type[4:-1]  # mem[\d+]

            program.append(Init(mask, int(index), int(value)))

    return program


def part1(input: str) -> int:
    program = parse_input(input)

    mem = collections.defaultdict(int)

    for init in program:
        value_i, mask_i, value = 1, -1, 0

        while value_i < SIZE:
            bit = init.value & value_i

            if init.mask[mask_i] == "X":
                value |= bit
            elif init.mask[mask_i] == "1":
                value |= value_i

            value_i <<= 1
            mask_i -= 1

        mem[init.address] = value

    return sum(mem.values())


def part2(input: str) -> int:
    program = parse_input(input)

    mem = collections.defaultdict(int)

    for init in program:
        mask: list[str | None] = []
        mask_floating: list[int] = []

        value_i, mask_i = 1, -1

        while value_i < SIZE:
            bit = init.address & value_i

            if init.mask[mask_i] == "0":
                mask.insert(0, str(int(bit != 0)))
            elif init.mask[mask_i] == "1":
                mask.insert(0, "1")
            else:
                mask.insert(0, None)
                mask_floating.append(mask_i)

            value_i <<= 1
            mask_i -= 1

        for i in range(2 ** len(mask_floating)):
            for j, k in itertools.zip_longest(
                mask_floating, reversed(bin(i)[2:]), fillvalue="0"
            ):
                mask[j] = k  # type: ignore

            mem[int("".join(mask), base=2)] = init.value  # type: ignore

    return sum(mem.values())


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
