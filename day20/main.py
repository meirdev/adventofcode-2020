# mypy: disable-error-code="union-attr"

import collections
import itertools
from typing import TypeAlias

Grid: TypeAlias = list[str]


MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]


def rotate(grid: Grid) -> Grid:
    return ["".join(row[::-1]) for row in zip(*grid)]


def flip(grid: Grid) -> Grid:
    return grid[::-1]


def get_orientations(grid: Grid) -> list[Grid]:
    grids = [grid]

    for _ in range(3):
        grids.append(rotate(grids[-1]))

    grids.append(flip(grid))

    for _ in range(3):
        grids.append(rotate(grids[-1]))

    return grids


def remove_edges(grid: Grid) -> Grid:
    return [row[1:-1] for row in grid[1:-1]]


def count_hashs(grid: Grid) -> int:
    return sum(row.count("#") for row in grid)


class Tile(collections.UserList[str]):
    def __init__(self, id: int, tile: list[str]) -> None:
        super().__init__(tile)

        self.id = id

        self.height = len(tile)
        self.width = len(tile[0])

        self.top = tile[0]
        self.bottom = tile[-1]
        self.left = "".join(row[0] for row in tile)
        self.right = "".join(row[-1] for row in tile)

    def __repr__(self) -> str:
        return f"{self.id}"


class Board(collections.UserList[list[Tile | None]]):
    def __init__(self, size: int) -> None:
        super().__init__([None] * size for _ in range(size))

        self.size = size


def parse_input(input: str) -> dict[int, Grid]:
    tiles = {}

    for tile in input.strip().split("\n\n"):
        title, tile = tile.split("\n", maxsplit=1)

        tiles[int(title[len("Tile ") : -1])] = tile.splitlines()

    return tiles


def solution(input: str) -> Board:
    tiles = parse_input(input)

    board = Board(int(len(tiles) ** 0.5))

    orientations = {i: [Tile(i, j) for j in get_orientations(tiles[i])] for i in tiles}

    used: set[int] = set()

    def inner(y: int, x: int) -> bool:
        if len(used) == len(tiles):
            return True

        for id, tiles_ in orientations.items():
            if id in used:
                continue

            for tile in tiles_:
                if (y - 1 >= 0 and board[y - 1][x].bottom != tile.top) or (
                    x - 1 >= 0 and board[y][x - 1].right != tile.left
                ):
                    continue

                board[y][x] = tile

                used.add(id)

                is_finished = (
                    inner(y + 1, 0) if x == board.size - 1 else inner(y, x + 1)
                )

                if is_finished:
                    return True

                used.remove(id)

                board[y][x] = None

        return False

    assert inner(0, 0)

    return board


def part1(input: str) -> int:
    board = solution(input)

    return board[0][0].id * board[0][-1].id * board[-1][0].id * board[-1][-1].id


def part2(input: str) -> int:
    board = solution(input)

    height = board[0][0].height - 2

    image = ["" for _ in range(board.size * height)]

    for y, row in enumerate(board):
        for tile in map(lambda i: remove_edges(i.data), row):
            for i in range(height):
                image[y * height + i] += tile[i]

    for board_ in get_orientations(image):
        monsters = sum(
            not any(
                MONSTER[h][w] == "#" and board_[y + h][x + w] != "#"
                for h in range(len(MONSTER))
                for w in range(len(MONSTER[h]))
            )
            for y, x in itertools.product(
                range(len(board_) - len(MONSTER) + 1),
                range(len(board_[i]) - len(MONSTER[0]) + 1),
            )
        )

        if monsters > 0:
            return count_hashs(image) - monsters * count_hashs(MONSTER)

    return -1


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
