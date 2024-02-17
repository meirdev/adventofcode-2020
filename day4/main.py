import re
from typing import Callable


FIELDS: dict[str, Callable[[str], bool]] = {
    "byr": lambda val: 1920 <= int(val) <= 2002,
    "iyr": lambda val: 2010 <= int(val) <= 2020,
    "eyr": lambda val: 2020 <= int(val) <= 2030,
    "hgt": lambda val: (
        (val[-2:] == "cm" and 150 <= int(val[:-2]) <= 193)
        or (val[-2:] == "in" and 59 <= int(val[:-2]) <= 76)
    ),
    "hcl": lambda val: re.fullmatch(r"#[0-9a-f]{6}", val) is not None,
    "ecl": lambda val: val in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda val: re.fullmatch(r"[0-9]{9}", val) is not None,
    "cid": lambda _: True,
}


def parse_input(input: str) -> list[dict[str, str]]:
    passports = []

    for passport in input.strip().split("\n\n"):
        fields = {}

        for line in passport.splitlines():
            for field in line.split(" "):
                key, value = field.split(":")
                fields[key] = value

        passports.append(fields)

    return passports


def solution(input: str, check_value: bool) -> int:
    passports = parse_input(input)

    return sum(
        1
        for passport in passports
        if all(
            key == "cid"
            or (key in passport and (not check_value or validator(passport[key])))
            for key, validator in FIELDS.items()
        )
    )


def part1(input: str) -> int:
    return solution(input, False)


def part2(input: str) -> int:
    return solution(input, True)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
