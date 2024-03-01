import enum
import itertools


class State(enum.StrEnum):
    ACTIVE = "#"
    INACTIVE = "."


def parse_input(input: str) -> list[list[State]]:
    return [list(map(State, line)) for line in input.strip().splitlines()]


def solution(input: str, dimensions: int):
    cubes_init = parse_input(input)

    cubes = {
        tuple([y, x] + [0] * (dimensions - 2))
        for y in range(len(cubes_init))
        for x in range(len(cubes_init[y]))
        if cubes_init[y][x] == State.ACTIVE
    }

    neighbors = list(itertools.product([-1, 0, 1], repeat=dimensions))
    neighbors.remove(tuple([0] * dimensions))

    for _ in range(6):
        limits = (
            range(
                min(cubes, key=lambda p: p[i])[i] - 1,
                max(cubes, key=lambda p: p[i])[i] + 2,
            )
            for i in range(dimensions)
        )

        temp_cubes = set()

        for cube in itertools.product(*limits):
            active = 0

            for neighbor in neighbors:
                n_cube = tuple(cube[i] + neighbor[i] for i in range(dimensions))

                if n_cube in cubes:
                    active += 1

                if active > 3:
                    break

            if (cube in cubes and active in [2, 3]) or (
                cube not in cubes and active == 3
            ):
                temp_cubes.add(cube)

        cubes = temp_cubes

    return len(cubes)


def part1(input: str) -> int:
    return solution(input, 3)


def part2(input: str) -> int:
    return solution(input, 4)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
