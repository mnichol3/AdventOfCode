"""Advent of Code 2024 - Day 6 Part 2"""
from bisect import insort, bisect
from collections import defaultdict
from itertools import cycle

from p1 import parse_input


def part2(guard_map: list[str]) -> int:
    """Solution to Part 2.

    Parameters
    ----------
    guard_map: list of str

    Returns
    -------
    int

    Problem Description
    -------------------
    * Same rules as Part 1:
        * If there is something directly in front of guard,
          turn right 90 degres.
        * Else, take one step forward.
    * Determine the number of positions an obstacle could be placed in order
      to form a closed loop of the guard's path.
        * Obstacle cannot be places on guard's starting position.

    Walkthrough
    -----------
    1. We no longer need to store visited positions.
    2. Move forward.
    3. If obstacle is encountered, turn 90 degrees right.
    4. Repeat 2 & 3 until 3 consecutive turns have been made.
    5. If
    """
    movement = cycle([
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ])

    ni = len(guard_map)
    nj = len(guard_map[0])
    obstacles = {
        'rows': defaultdict(list),
        'cols': defaultdict(list),
    }

    for i in range(ni):
        for j in range(nj):
            if guard_map[i][j] == '#':
                insort(obstacles['rows'][i], j)
                insort(obstacles['cols'][j], i)
            if guard_map[i][j] == '^':
                start = (i, j, 'up')

    def move(i, j, v, obstacles):
        i_obs = obstacles['rows'][i]
        j_obs = obstacles['cols'][j]

        if v == 'up':
            if not j_obs or j_obs[0] > i:
                new_i = -1
            else:
                ii = bisect(j_obs, i)
                new_i = j_obs[ii-1] + 1
            return new_i, j, 'right'

        if v == 'right':
            if not i_obs or i_obs[-1] < j:
                new_j = nj
            else:
                ii = bisect(i_obs, j)
                new_j = i_obs[ii] - 1
            return i, new_j, 'down'

        if v == 'down':
            if not j_obs or j_obs[-1] < i:
                new_i = ni
            else:
                ii = bisect(j_obs, i)
                new_i = j_obs[ii] - 1
            return new_i, j, 'left'

        if v == 'left':
            if not i_obs or i_obs[0] > j:
                new_j = -1
            else:
                ii = bisect(i_obs, j)
                new_j = i_obs[ii-1] + 1
            return i, new_j, 'up'

    candidates = set()
    i, j, v = start
    while i in range(ni) and j in range(nj):
        new_i, new_j, new_v = move(i, j, v, obstacles)
        if v == 'up':
            candidates |= set((i, j) for i in range(new_i+1, i+1))
        elif v == 'right':
            candidates |= set((i, j) for j in range(j, new_j))
        elif v == 'down':
            candidates |= set((i, j) for i in range(i, new_i))
        elif v == 'left':
            candidates |= set((i, j) for j in range(new_j+1, j+1))
        i, j, v = new_i, new_j, new_v

    def is_looping(obstacles):
        i, j, v = start
        visited = set([start])
        while i in range(ni) and j in range(nj):
            i, j, v = move(i, j, v, obstacles)
            if (i, j, v) in visited:
                return True
            visited.add((i, j, v))
        return False

    loop_count = 0
    for i, j in candidates:
        insort(obstacles['rows'][i], j)
        insort(obstacles['cols'][j], i)
        loop_count += is_looping(obstacles)
        obstacles['rows'][i].remove(j)
        obstacles['cols'][j].remove(i)

    return loop_count


if __name__ == '__main__':
    print(f'Day 06 Part 2 answer: {part2(parse_input())}')
    # 1576 too low