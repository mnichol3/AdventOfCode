"""Advent of Code 2024 - Day 6 Part 1"""
from itertools import cycle
from pathlib import Path


def parse_input(fname: str = None) -> list[str]:
    """Parse the input from a text file.

    Parameters
    ----------
    None.

    Returns
    -------
    list of str
    """
    fname = 'input.txt' if fname is None else fname

    return [x for x in Path(fname).read_text().split('\n') if x]


def part1(guard_map: list[str]) -> int:
    """Solution to Part 1.

    Parameters
    ----------
    guard_map: list of str

    Returns
    -------
    int

    Problem Description
    -------------------
    * If there is something directly in front of guard, turn right 90 degres.
    * Else, take one step forward.
    * Including the guard's starting position, track distinct positions visited
      until the guard exits the map.

    Walkthrough
    -----------
    1. Store position.
    2. Move forward.
    3. If obstacle is encountered, turn 90 degrees right.
    4. Repeat 2 & 3 until exiting map.
    5. Get unique map coordinates.
    """

    def get_starting_pos(guard_map: list[str]) -> tuple[int, int]:
        for i in range(len(guard_map)):
            for j in range(len(guard_map[0])):
                if guard_map[i][j] == '^':
                    return i, j

        return -1, -1

    movement = cycle([
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ])

    ni = len(guard_map)
    nj = len(guard_map[0])

    curr_i, curr_j = get_starting_pos(guard_map)

    if (curr_i, curr_j) == (-1, -1):
        return 0

    visited = set([(curr_i, curr_j)])
    move = next(movement)
    while True:
        next_i = curr_i + move[0]
        next_j = curr_j + move[1]

        if not 0 <= next_i < ni or not 0 <= next_j < nj:
            return len(visited)

        if guard_map[next_i][next_j] == '#':
            move = next(movement)
        else:
            curr_i = next_i
            curr_j = next_j
            visited.add((curr_i, curr_j))


if __name__ == '__main__':
    print(f'Day 06 Part 1 answer: {part1(parse_input("input.txt"))}')
