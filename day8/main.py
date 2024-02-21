from typing import NamedTuple


class Instruction(NamedTuple):
    operation: str
    argument: int


def parse_input(input: str) -> list[Instruction]:
    instructions = []

    for line in input.strip().splitlines():
        operation, argument = line.split(" ")

        instructions.append(Instruction(operation, int(argument)))

    return instructions


def run(instructions: list[Instruction]) -> tuple[bool, int]:
    i, visited = 0, set()

    exit_status = True

    accumulator = 0

    while i < len(instructions):
        if i in visited:
            exit_status = False
            break

        visited.add(i)

        match instructions[i]:
            case "acc", value:
                accumulator += value
            case "jmp", location:
                i += location
                continue
            case _:
                pass

        i += 1

    return exit_status, accumulator


def part1(input: str) -> int:
    instructions = parse_input(input)

    _, accumulator = run(instructions)

    return accumulator


def part2(input: str) -> int | None:
    instructions = parse_input(input)

    table = {"nop": "jmp", "jmp": "nop"}

    for i in range(len(instructions)):
        operation, argument = instructions[i]

        if operation in table:
            instructions_ = instructions[:]
            instructions_[i] = Instruction(table[operation], argument)

            exit_code, accumulator = run(instructions_)
            if exit_code:
                return accumulator

    return None


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
