import functools
import math
import re
from typing import NamedTuple, TypeAlias


Ticket: TypeAlias = list[int]


class Range(NamedTuple):
    start: int
    end: int

    def __contains__(self, key: object) -> bool:
        if isinstance(key, int):
            return self.start <= key <= self.end

        raise NotImplementedError


def parse_input(input: str) -> tuple[dict[str, list[Range]], Ticket, list[Ticket]]:
    match = re.match(
        r"(?P<fields>.+?)\n\nyour ticket:\n(?P<your_ticket>.+?)\n\nnearby tickets:\n(?P<nearby_tickets>.+)",
        input.strip(),
        re.DOTALL,
    )

    if match is None:
        raise ValueError("invalid input")

    your_ticket, *nearby_tickets = [
        [int(number) for number in ticket.split(",")]
        for key in ("your_ticket", "nearby_tickets")
        for ticket in match.group(key).splitlines()
    ]

    fields: dict[str, list[Range]] = {}

    for field in match.group("fields").splitlines():
        name, ranges = field.split(":")
        fields[name] = [
            Range(int(start), int(end))
            for start, end in re.findall(r"(\d+)-(\d+)", ranges)
        ]

    return fields, your_ticket, nearby_tickets


def part1(input: str) -> int:
    fields, _, nearby_tickets = parse_input(input)

    not_valid = []

    for nearby_ticket in nearby_tickets:
        for num in nearby_ticket:
            if not any(
                num in range_ for ranges in fields.values() for range_ in ranges
            ):
                not_valid.append(num)

    return sum(not_valid)


def part2(input: str, startswith: str = "departure") -> int:
    fields, your_ticket, nearby_tickets = parse_input(input)

    valid_names = []

    for nearby_ticket in nearby_tickets:
        ticket = []

        for num in nearby_ticket:
            names = [
                name
                for name, ranges in fields.items()
                for range_ in ranges
                if num in range_
            ]

            if len(names) == 0:
                break

            ticket.append(names)
        else:
            valid_names.append(ticket)

    valid_names_cols = [
        functools.reduce(lambda a, b: set(a) & set(b), i) for i in zip(*valid_names)
    ]

    cols: dict[int, str] = {}

    while len(cols) != len(fields):
        certain = {
            i: col.pop() for i, col in enumerate(valid_names_cols) if len(col) == 1
        }

        cols |= certain

        for row in valid_names_cols:
            row -= set(certain.values())

    return math.prod(
        your_ticket[i] for i, name in cols.items() if name.startswith(startswith)
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
