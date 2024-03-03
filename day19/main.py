from typing import TypeAlias


Rule: TypeAlias = str | list[list[str]]


def parse_input(input: str) -> tuple[dict[str, Rule], list[str]]:
    rules_, messages_ = input.strip().split("\n\n")

    rules: dict[str, Rule] = {}

    for id, rule in map(lambda i: i.split(":"), rules_.splitlines()):
        if '"' in rule:
            rules[id] = rule.strip()[1:-1]
        else:
            rules[id] = [sub_rule.strip().split(" ") for sub_rule in rule.split("|")]

    messages = messages_.splitlines()

    return rules, messages


def solution(rules: dict[str, Rule], messages: list[str]) -> int:
    def run(rule: str | list[str], message: str):
        if not rule:
            yield message
        elif isinstance(rule, list):
            for message in run(rule[0], message):
                yield from run(rule[1:], message)
        elif isinstance(rules[rule], list):
            for rule_ in rules[rule]:
                yield from run(rule_, message)
        elif message and message[0] == rules[rule]:
            yield message[1:]

    return sum(any(m == "" for m in run("0", msg)) for msg in messages)


def part1(input: str) -> int:
    rules, messages = parse_input(input)

    return solution(rules, messages)


def part2(input: str) -> int:
    rules, messages = parse_input(input)

    rules = {
        **rules,
        "8": [["42"], ["42", "8"]],
        "11": [["42", "31"], ["42", "11", "31"]],
    }

    return solution(rules, messages)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
