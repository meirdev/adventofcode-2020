import enum
import itertools


class State(enum.StrEnum):
    ACTIVE = "#"
    INACTIVE = "."


def parse_input(input: str) -> list[list[State]]:
    return [list(map(State, line)) for line in input.strip().splitlines()]


def part1(input: str) -> int:
    cubes_init = parse_input(input)

    neighbors = list(itertools.product([-1, 0, 1], repeat=3))
    neighbors.remove((0, 0, 0))

    cubes = {
        (y, x, 0)
        for y in range(len(cubes_init))
        for x in range(len(cubes_init[y]))
        if cubes_init[y][x] == State.ACTIVE
    }

    for _ in range(6):
        y_min = min(cubes, key=lambda p: p[0])[0] - 1
        y_max = max(cubes, key=lambda p: p[0])[0] + 1
        x_min = min(cubes, key=lambda p: p[1])[1] - 1
        x_max = max(cubes, key=lambda p: p[1])[1] + 1
        z_min = min(cubes, key=lambda p: p[2])[2] - 1
        z_max = max(cubes, key=lambda p: p[2])[2] + 1

        temp_cubes = set()

        for z in range(z_min, z_max + 1):
            for y in range(y_min, y_max + 1):
                for x in range(x_min, x_max + 1):
                    cube = (y, x, z)

                    active = 0

                    for ny, nx, nz in neighbors:
                        n_cube = (ny + y, nx + x, nz + z)

                        if n_cube in cubes:
                            active += 1

                    if (cube in cubes and active in [2, 3]) or (
                        cube not in cubes and active == 3
                    ):
                        temp_cubes.add(cube)

        cubes = temp_cubes

    return len(cubes)


def part2(input: str) -> int:
    cubes_init = parse_input(input)

    neighbors = list(itertools.product([-1, 0, 1], repeat=4))
    neighbors.remove((0, 0, 0, 0))

    cubes = {
        (y, x, 0, 0)
        for y in range(len(cubes_init))
        for x in range(len(cubes_init[y]))
        if cubes_init[y][x] == State.ACTIVE
    }

    for _ in range(6):
        y_min = min(cubes, key=lambda p: p[0])[0] - 1
        y_max = max(cubes, key=lambda p: p[0])[0] + 1
        x_min = min(cubes, key=lambda p: p[1])[1] - 1
        x_max = max(cubes, key=lambda p: p[1])[1] + 1
        z_min = min(cubes, key=lambda p: p[2])[2] - 1
        z_max = max(cubes, key=lambda p: p[2])[2] + 1
        w_min = min(cubes, key=lambda p: p[3])[3] - 1
        w_max = max(cubes, key=lambda p: p[3])[3] + 1

        temp_cubes = set()

        for w in range(w_min, w_max + 1):
            for z in range(z_min, z_max + 1):
                for y in range(y_min, y_max + 1):
                    for x in range(x_min, x_max + 1):
                        cube = (y, x, z, w)

                        active = 0

                        for ny, nx, nz, nw in neighbors:
                            n_cube = (ny + y, nx + x, nz + z, nw + w)

                            if n_cube in cubes:
                                active += 1

                        if (cube in cubes and active in [2, 3]) or (
                            cube not in cubes and active == 3
                        ):
                            temp_cubes.add(cube)

        cubes = temp_cubes

    return len(temp_cubes)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
