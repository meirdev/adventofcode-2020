from .main import part1, part2


INPUT = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""


def test_part1():
    assert part1(INPUT) == 5


def test_part2():
    assert part2(INPUT) == "mxmxvkd,sqjhc,fvjkl"


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 2150
    assert part2(input) == "vpzxk,bkgmcsx,qfzv,tjtgbf,rjdqt,hbnf,jspkl,hdcj"
