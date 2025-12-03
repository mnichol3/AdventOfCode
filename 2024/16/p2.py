"""Advent of Code 2024 - Day 16 Part 2"""
from queue import PriorityQueue

from p1 import *


class Solution2(Solution):

    def __init__(self, maze: list[list[str]]) -> None:
        super().__init__(maze)
        self.start, self.end = self._get_start_end()
        self.paths = []

    def solve2(self) -> tuple[int, int]:
        q = PriorityQueue()
        q.put(Reindeer(self.start, 0, Move.EAST.value, set()))

        costs = {}
        min_cost = float('inf')
        min_paths = set()

        while not q.empty():
            reindeer = q.get()

            for neighbor in self.get_neighbors(reindeer.pos):
                if reindeer.cost > min_cost:
                    continue

                curr_cost = costs.get(
                    (reindeer.pos, reindeer.direction), float('inf'))

                if curr_cost < reindeer.cost:
                    continue

                costs[(reindeer.pos, reindeer.direction)] = reindeer.cost

                curr_cost = update_cost(reindeer, neighbor)
                curr_dir = subtract(neighbor, reindeer.pos)

                if neighbor == self.end:
                    if curr_cost < min_cost:
                        min_cost = curr_cost
                        min_paths = set(reindeer.visited)
                    elif curr_cost == min_cost:
                        min_paths |= reindeer.visited
                elif neighbor not in reindeer.visited:
                    visited2 = reindeer.visited.copy()
                    visited2.add(neighbor)
                    if curr_cost < min_cost:
                        q.put(Reindeer(neighbor, curr_cost, curr_dir, visited2))

        return min_cost, len(min_paths) + 2


if __name__ == '__main__':
    soln = Solution2(parse_input())
    min_cost, common_pos = soln.solve2()
    print(f"Part 2 answer: {common_pos}")
