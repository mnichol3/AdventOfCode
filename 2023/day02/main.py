"""
Advent of Code 2023
Day 2 - Cube Conundrum
"""
import re
from pathlib import Path


SAMPLE_INP = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
]


MAX_COUNT = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


CUBE_PATT = r'(\d+)\s(\w+)'


def split_game(game_str: str) -> tuple[int, list[str]]:
    game_num, draws = game_str.split(':')
    draws = draws.strip().split(';')
    id = int(game_num.split(' ')[1])

    return id, draws


def solve_1(games: list[str]) -> int:
    valid_games = []

    for curr_game in games:
        valid = []
        id, draws = split_game(curr_game)

        for d in draws:
            cube_cnt = {
                key: int(val) for (val, key) in re.findall(CUBE_PATT, d)
            }

            valid.append(
                all([MAX_COUNT[key] >= val for (key, val) in cube_cnt.items()])
            )

        if all(valid): valid_games.append(id)

    return sum(valid_games)


def solve_2(games: list[str]) -> int:
    powers = []

    for curr_game in games:
        id, draws = split_game(curr_game)

        cube_cnt = {key: 0 for key in ['red', 'green', 'blue']}

        for d in draws:
            curr_cnt = {
                key: int(val) for (val, key) in re.findall(CUBE_PATT, d)
            }

            for key, val in curr_cnt.items():
                if val > cube_cnt[key]:
                    cube_cnt[key] = val

        vals = list(cube_cnt.values())
        prod = vals[0]
        for x in vals[1:]:
            prod *= x

        powers.append(prod)

    return sum(powers)


if __name__ == '__main__':
    input = Path(__file__).with_name('input.txt').read_text().splitlines()
    #print(solve_1(input))
    print(solve_2(input))
