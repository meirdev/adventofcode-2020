import collections
import enum
import functools


class Neighbor(enum.StrEnum):
    EAST = "e"
    SOUTHEAST = "se"
    SOUTHWEST = "sw"
    WEST = "w"
    NORTHWEST = "nw"
    NORTHEAST = "ne"


def get_neighbor_value(neighbor: Neighbor) -> tuple[int, int]:
    # x, y
    match neighbor:
        case Neighbor.EAST:
            return 2, 0
        case Neighbor.SOUTHEAST:
            return 1, -1
        case Neighbor.SOUTHWEST:
            return -1, -1
        case Neighbor.WEST:
            return -2, 0
        case Neighbor.NORTHWEST:
            return -1, 1
        case Neighbor.NORTHEAST:
            return 1, 1


def parse_input(input: str) -> list[list[Neighbor]]:
    tiles = []

    for line in input.strip().splitlines():
        i = 0

        tile = []

        while i < len(line):
            try:
                tile.append(Neighbor(line[i]))
                i += 1
            except:
                tile.append(Neighbor(line[i : i + 2]))
                i += 2

        tiles.append(tile)

    return tiles


def get_adjacents(hex: tuple[int, int]) -> set[tuple[int, int]]:
    adjacents = set()

    for neighbor in Neighbor:
        value = get_neighbor_value(neighbor)
        adjacents.add((hex[0] + value[0], hex[1] + value[1]))

    return adjacents


def get_black_tiles(input: str) -> set[tuple[int, int]]:
    tiles = parse_input(input)

    counter = collections.Counter(
        functools.reduce(
            lambda a, b: (a[0] + b[0], a[1] + b[1]),
            map(get_neighbor_value, tile),
            (0, 0),
        )
        for tile in tiles
    )

    return {i for i in counter if counter[i] % 2 != 0}


def part1(input: str) -> int:
    black_tiles = get_black_tiles(input)

    return len(black_tiles)


def part2(input: str) -> int:
    black_tiles = get_black_tiles(input)

    for _ in range(100):
        tiles = set()

        temp_black = set()

        for tile in black_tiles:
            i = 0

            for adjacent in get_adjacents(tile):
                if adjacent in black_tiles:
                    i += 1
                tiles.add(adjacent)

            if not (i == 0 or i > 2):
                temp_black.add(tile)

        for tile in tiles - black_tiles:
            i = 0

            for adjacent in get_adjacents(tile):
                if adjacent in black_tiles:
                    i += 1

            if i == 2:
                temp_black.add(tile)

        black_tiles = temp_black

    return len(temp_black)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
