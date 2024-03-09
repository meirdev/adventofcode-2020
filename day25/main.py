import itertools


def parse_input(input: str) -> list[int]:
    return list(map(int, input.strip().splitlines()))


def transform(
    subject: int, stop_value: int | None = None, stop_index: int | None = None
) -> int:
    value = 1

    for i in itertools.count(1):
        value = value * subject % 20201227

        if stop_value and value == stop_value:
            return i

        if stop_index and i == stop_index:
            return value

    return -1


def part1(input: str) -> int:
    card_pub_key, door_pub_key = parse_input(input)

    card_loop_size = transform(7, stop_value=card_pub_key)
    door_loop_size = transform(7, stop_value=door_pub_key)

    enc_key1 = transform(door_pub_key, stop_index=card_loop_size)
    enc_key2 = transform(card_pub_key, stop_index=door_loop_size)

    assert enc_key1 == enc_key2

    return enc_key1


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))


if __name__ == "__main__":
    main()
