import enum
import itertools


class Type(enum.StrEnum):
    FLOOR = "."
    EMPTY_SEAT = "L"
    OCCUPIED_SEAT = "#"


DIRECTIONS = [i for i in itertools.product(range(-1, 2), repeat=2) if i != (0, 0)]


def parse_input(input: str) -> list[list[Type]]:
    grid = []

    for row in input.strip().splitlines():
        grid.append(list(map(Type, row)))

    return grid


def count_occupied_seats(
    grid: list[list[Type]], adjacent: bool, origin_y: int, origin_x: int
) -> int:
    occupied = 0

    for yi, xi in DIRECTIONS:
        y, x = origin_y, origin_x

        while 0 <= (y := y + yi) < len(grid) and 0 <= (x := x + xi) < len(grid[y]):
            if grid[y][x] == Type.OCCUPIED_SEAT:
                occupied += 1
                break

            if grid[y][x] != Type.FLOOR or adjacent:
                break

    return occupied


def solution(input: str, adjacent_only: bool) -> int:
    grid = parse_input(input)

    if adjacent_only:
        occupied_seats = 4
    else:
        occupied_seats = 5

    changed = True

    while changed:
        changed = False

        new_grid = []

        for y, row in enumerate(grid):
            new_grid.append(row[:])

            for x, col in enumerate(row):
                if (
                    col == Type.EMPTY_SEAT
                    and count_occupied_seats(grid, adjacent_only, y, x) == 0
                ):
                    new_grid[y][x] = Type.OCCUPIED_SEAT
                    changed = True

                elif (
                    col == Type.OCCUPIED_SEAT
                    and count_occupied_seats(grid, adjacent_only, y, x)
                    >= occupied_seats
                ):
                    new_grid[y][x] = Type.EMPTY_SEAT
                    changed = True

        grid = new_grid

    return sum(
        1 for i in itertools.chain.from_iterable(grid) if i == Type.OCCUPIED_SEAT
    )


def part1(input: str) -> int:
    return solution(input, adjacent_only=True)


def part2(input: str) -> int:
    return solution(input, adjacent_only=False)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
