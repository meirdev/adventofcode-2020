import enum
from typing import NamedTuple


class ActionType(enum.StrEnum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    LEFT = "L"
    RIGHT = "R"
    FORWARD = "F"


class Action(NamedTuple):
    type: ActionType
    value: int


FORWARD = {
    ActionType.NORTH: (0, -1),
    ActionType.SOUTH: (0, 1),
    ActionType.WEST: (-1, 0),
    ActionType.EAST: (1, 0),
}


FACE_CLOCKWISE = [
    ActionType.NORTH,
    ActionType.EAST,
    ActionType.SOUTH,
    ActionType.WEST,
]


def parse_input(input: str) -> list[Action]:
    return [Action(ActionType(i[0]), int(i[1:])) for i in input.strip().splitlines()]


def part1(input: str) -> int:
    actions = parse_input(input)

    ship_face, x, y = ActionType.EAST, 0, 0

    for type, value in actions:
        match type:
            case ActionType.NORTH:
                y -= value
            case ActionType.SOUTH:
                y += value
            case ActionType.WEST:
                x -= value
            case ActionType.EAST:
                x += value
            case ActionType.FORWARD:
                x_, y_ = FORWARD[ship_face]
                x += x_ * value
                y += y_ * value
            case ActionType.RIGHT:
                k = value // 90
                ship_face = FACE_CLOCKWISE[
                    (FACE_CLOCKWISE.index(ship_face) + k) % len(FACE_CLOCKWISE)
                ]
            case ActionType.LEFT:
                k = value // 90
                ship_face = FACE_CLOCKWISE[
                    (FACE_CLOCKWISE.index(ship_face) - k) % len(FACE_CLOCKWISE)
                ]

    return abs(x) + abs(y)


def part2(input: str) -> int:
    actions = parse_input(input)

    x, y = 0, 0
    waypoint_x, waypoint_y = 10, -1

    for type, value in actions:
        match type:
            case ActionType.NORTH:
                waypoint_y -= value
            case ActionType.SOUTH:
                waypoint_y += value
            case ActionType.WEST:
                waypoint_x -= value
            case ActionType.EAST:
                waypoint_x += value
            case ActionType.FORWARD:
                x += waypoint_x * value
                y += waypoint_y * value
            case ActionType.RIGHT:
                for _ in range(value // 90):
                    waypoint_x, waypoint_y = -waypoint_y, waypoint_x
            case ActionType.LEFT:
                for _ in range(value // 90):
                    waypoint_x, waypoint_y = waypoint_y, -waypoint_x

    return abs(x) + abs(y)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
