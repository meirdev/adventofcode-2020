import collections
from typing import Deque, TypeAlias

Deck: TypeAlias = list[int]

PLAYER_1 = 0
PLAYER_2 = 1


def parse_input(input: str) -> list[Deck]:
    players = input.strip().split("\n\n")

    return [list(map(int, player.splitlines()[1:])) for player in players]


def score(deck: Deque[int]) -> int:
    return sum(i * card for i, card in enumerate(reversed(deck), start=1))


def play_game(deck1: Deck, deck2: Deck, recursive: bool = False) -> tuple[int, int]:
    decks = (collections.deque(deck1), collections.deque(deck2))

    visited = set()

    while True:
        key = tuple(decks[PLAYER_1]), tuple(decks[PLAYER_2])

        if key in visited:
            return PLAYER_1, score(decks[PLAYER_1])

        visited.add(key)

        if len(decks[PLAYER_1]) == 0:
            return PLAYER_2, score(decks[PLAYER_2])
        elif len(decks[PLAYER_2]) == 0:
            return PLAYER_1, score(decks[PLAYER_1])

        card1 = decks[PLAYER_1].popleft()
        card2 = decks[PLAYER_2].popleft()

        if (
            recursive
            and len(decks[PLAYER_1]) >= card1
            and len(decks[PLAYER_2]) >= card2
        ):
            if (
                play_game(
                    list(decks[PLAYER_1])[:card1],
                    list(decks[PLAYER_2])[:card2],
                    recursive=True,
                )[0]
                == 0
            ):
                decks[PLAYER_1].extend([card1, card2])
            else:
                decks[PLAYER_2].extend([card2, card1])
        else:
            if card1 > card2:
                decks[PLAYER_1].extend([card1, card2])
            else:
                decks[PLAYER_2].extend([card2, card1])


def part1(input: str) -> int:
    decks = parse_input(input)

    return play_game(decks[PLAYER_1], decks[PLAYER_2], recursive=False)[1]


def part2(input: str) -> int:
    decks = parse_input(input)

    return play_game(decks[PLAYER_1], decks[PLAYER_2], recursive=True)[1]


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
