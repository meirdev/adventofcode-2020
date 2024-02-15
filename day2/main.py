import collections
import contextlib
import re
from typing import Callable, NamedTuple


class PasswordPolicy(NamedTuple):
    a: int
    b: int
    char: str

    def is_valid_1(self, password: str) -> bool:
        return self.a <= collections.Counter(password)[self.char] <= self.b

    def is_valid_2(self, password: str) -> bool:
        found = 0

        with contextlib.suppress(IndexError):
            found += self.char == password[self.a - 1]

        with contextlib.suppress(IndexError):
            found += self.char == password[self.b - 1]

        return found == 1


def parse_input(input: str) -> list[tuple[PasswordPolicy, str]]:
    passswords = []

    for a, b, char, password in re.findall(r"(\d+)-(\d+) (\w): (\w+)", input):
        passswords.append((PasswordPolicy(int(a), int(b), char), password))

    return passswords


def solution(input: str, validator: Callable[[PasswordPolicy, str], bool]) -> int:
    passswords = parse_input(input)

    return sum(1 for policy, password in passswords if validator(policy, password))


def part1(input: str) -> int:
    return solution(input, PasswordPolicy.is_valid_1)


def part2(input: str) -> int:
    return solution(input, PasswordPolicy.is_valid_2)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
