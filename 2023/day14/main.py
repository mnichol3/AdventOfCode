"""
Advent of Code 2023
Day 14 - Parabolic Reflector Dish
"""
from pathlib import Path


SAMPLE_GRID = [
    'O....#....',
    'O.OO#....#',
    '.....##...',
    'OO.#O....O',
    '.O.....O#.',
    'O.#..O.#.#',
    '..O..#O..O',
    '.......O..',
    '#....###..',
    '#OO..#....',
]


# North, West, South, East
TILTS = {
    1: (-1, 0),
    2: (0, -1),
    3: (1, 0),
    4: (0, 1),
}


def pretty_print(grid: list[list[str]]) -> None:
    [print(''.join(x)) for x in grid]
    print('-'*20)


def explode(grid: list[str]) -> list[list[str]]:
    return [list(x) for x in grid]


def solve_2(grid: list[list[str]], cycles: int = 10e8, pprint: bool = False) -> int:
    """Solution to Part 2."""
    n_rows = len(grid)
    n_cols = len(grid[0])

    # GIVE ME MORE LOOPS I LOVE LOOPS
    for cyc in range(cycles):
        for k in range(1, 5, 1):
            delta_i, delta_j = TILTS[k]

            for i in range(n_rows):
                for j in range(n_cols):
                    if (
                        grid[i][j] == 'O' and
                        i + delta_i >= 0 and
                        j + delta_j >= 0
                    ):
                        ii, jj = i, j

                        try:
                            next_spot = grid[ii + delta_i][jj + delta_j]
                        except IndexError:
                            continue

                        while (
                            next_spot == '.' and
                            ii + delta_i >= 0 and
                            jj + delta_j >= 0
                        ):

                            try:
                                grid[ii + delta_i][jj + delta_j] = 'O'
                            except IndexError:
                                break

                            grid[ii][jj] = '.'

                            ii += delta_i
                            jj += delta_j

                            next_spot = grid[ii][jj]
                # end j
            # end i
        # end tilt loop
    # end cycle loop

    sum = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 'O': sum += n_rows - i

    if pprint: pretty_print(grid)

    return sum


def solve_1(grid: list[list[str]], pprint: bool = False) -> int:
    """Solution to Part 1."""
    n_rows = len(grid)
    n_cols = len(grid[0])

    for i in range(n_rows):
        for j in range(n_cols):

            if grid[i][j] == 'O':
                ii, jj = i, j

                while grid[ii - 1][jj] == '.' and ii > 0:
                    grid[ii][jj] = '.'
                    ii -= 1
                    grid[ii][jj] = 'O'

    sum = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 'O': sum += n_rows - i

    if pprint: pretty_print(grid)

    return sum


if __name__ == '__main__':
    grid = explode(SAMPLE_GRID)
    #grid = explode(Path(__file__).with_name('input.txt').read_text().splitlines())

    #soln= solve_1(grid)
    soln = solve_2(grid, cycles=1, pprint=True)

    print(soln)

