"""Advent of Code 2024 - Day 15 Part 2"""
from p1 import Fishtank, parse_input


class UpdatedFishtank(Fishtank):

    def __init__(self, tank_map: list[list[str]]) -> None:
        self.grid = tank_map
        self._resize_grid()
        self.num_i, self.num_j = self._set_dims()
        self.robot_pos = self._get_init_pos()
        self.part = 2

    def _resize_grid(self):
        _mapping = {
            '#': '##',
            'O': '[]',
            '.': '..',
            '@': '@.',
        }
        self.grid = [list("".join(_mapping[c] for c in line))
                     for line in self.grid]


def part2(f_path: str = 'input.txt') -> int:
    """Solution to Part 2."""
    tank_map, moves = parse_input(f_path)
    fishtank = UpdatedFishtank(tank_map)

    for m in moves:
        fishtank.move_robot(m)

    return sum(
        100 * i + j for i in range(fishtank.num_i)
        for j in range(fishtank.num_j) if fishtank.grid[i][j] == '[')


if __name__ == '__main__':
    print(f'Part 2 answer: {part2()}')
