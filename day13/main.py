import math


def parse_input(input: str) -> tuple[int, list[str]]:
    timestamp, bus_ids = input.strip().splitlines()

    return int(timestamp), bus_ids.split(",")


def get_id_offsets(bus_ids: list[str]) -> list[tuple[int, int]]:
    return [(int(id), i) for i, id in enumerate(bus_ids) if id != "x"]


def part1(input: str) -> int:
    timestamp, bus_ids = parse_input(input)

    return math.prod(
        min(
            (
                (id, (timestamp // id + 1) * id - timestamp)
                for id, _ in get_id_offsets(bus_ids)
            ),
            key=lambda i: i[1],  # type: ignore
        )
    )


def part2(input: str) -> int:
    _, bus_ids = parse_input(input)

    id_offsets = get_id_offsets(bus_ids)

    position, increment = 0, id_offsets[0][0]

    for id, offset in id_offsets[1:]:

        while (position + offset) % id != 0:
            position += increment

        increment = math.lcm(increment, id)

    return position


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
