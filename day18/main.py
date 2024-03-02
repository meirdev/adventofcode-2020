import re
from typing import Literal, TypeAlias


Expression: TypeAlias = list[Literal["*", "+", "(", ")"] | int]


def parse_input(input: str) -> list[Expression]:
    expressions: list[Expression] = []

    for line in input.strip().splitlines():
        line = re.sub(r"\s+", "", line)

        expression: Expression = []

        for token in re.findall(r"([^\d]|\d+)", line):
            if token not in ("*", "+", "(", ")"):
                expression.append(int(token))
            else:
                expression.append(token)

        expressions.append(expression)

    return expressions


def solve(expression: Expression, precedence: bool) -> int:

    def inner(i: int = 0) -> tuple[int, int]:
        expression_ = []

        while i < len(expression):
            if expression[i] == "(":
                i, ret = inner(i + 1)
                expression_.append(ret)
            elif expression[i] == ")":
                i += 1
                break
            else:
                expression_.append(expression[i])  # type: ignore
                i += 1

        if precedence:
            k = 0
            while k < len(expression_):
                if expression_[k] == "+":
                    expression_[k - 1 : k + 2] = [
                        expression_[k - 1] + expression_[k + 1]
                    ]
                else:
                    k += 1

        result = expression_[0]

        for j in range(1, len(expression_), 2):
            if expression_[j] == "*":
                result *= expression_[j + 1]
            elif expression_[j] == "+":
                result += expression_[j + 1]

        return i, result

    return inner()[1]


def solution(input: str, precedence: bool) -> int:
    expressions = parse_input(input)

    return sum(map(lambda e: solve(e, precedence), expressions))


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
