import collections
import functools
import re
from typing import Counter, NamedTuple


class Food(NamedTuple):
    ingredients: set[str]
    allergens: set[str]


def parse_input(input: str) -> list[Food]:
    foods = []

    for ingredients, allergens in re.findall(r"(.*?) \(contains (.*?)\)", input):
        foods.append(Food(set(ingredients.split(" ")), set(allergens.split(", "))))

    return foods


def solution(input: str) -> tuple[Counter[str], dict[str, set[str]]]:
    foods = parse_input(input)

    allergen_ingredients: dict[str, set[str]] = {}

    ingredients: Counter[str] = collections.Counter()

    for food in foods:
        for allergen in food.allergens:
            if allergen not in allergen_ingredients:
                allergen_ingredients[allergen] = set(food.ingredients)
            else:
                allergen_ingredients[allergen] &= food.ingredients

        ingredients.update(food.ingredients)

    return ingredients, allergen_ingredients


def part1(input: str) -> int:
    ingredients, allergen_ingredients = solution(input)

    ingredients_with_allergens = functools.reduce(
        lambda a, b: a | b, allergen_ingredients.values()
    )

    return sum(
        ingredients[i] for i in ingredients if i not in ingredients_with_allergens
    )


def part2(input: str) -> str:
    _, allergen_ingredients = solution(input)

    ingredients_used = set()
    ingredients_by_allergen = {}

    while (
        allergen := next(
            (i for i in allergen_ingredients if len(allergen_ingredients[i]) == 1), None
        )
    ) is not None:
        ingredients_by_allergen[allergen] = allergen_ingredients[allergen].pop()

        ingredients_used.add(ingredients_by_allergen[allergen])

        for ingredients in allergen_ingredients.values():
            ingredients -= ingredients_used

    return ",".join(ingredients_by_allergen[i] for i in sorted(ingredients_by_allergen))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
