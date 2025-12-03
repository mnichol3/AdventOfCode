"""Advent of Code 2024 - Day 20 Part 2"""
from p1 import calc_distance, parse_input, Maze, Point


def get_distance(a: Point, b: Point, max_diff: int = 20) -> int | None:
        """Return the manhattan distance if within the valid max value."""
        dist = calc_distance(a, b)

        if dist > max_diff:
             return None

        return dist


def find_shortcuts(best_path: list[Point], length: int = 2) -> int:
    """Find possible shortcuts in the best path.

    Parameters
    ----------
    best_path: list of tuple of (int, int)
        Coordinates of the computed best path.
    length: int, optional
        Maximum length of the cheat/shortcut. Default is 2.

    Returns
    -------
    int
    """
    n_cheats = 0

    for idx, point1 in enumerate(best_path):
        for idx2 in range(idx+100+1, len(best_path)):
            point2 = best_path[idx2]
            dist = get_distance(point1, point2, length)
            if dist:
                n_cheats += (idx2 - idx - dist) >= 100

    return n_cheats


if __name__ == '__main__':
    maze = Maze(parse_input())
    path = maze.bfs()

    print(f'Part 2 answer: {find_shortcuts(path, length=20)}')
