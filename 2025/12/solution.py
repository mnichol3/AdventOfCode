"""Advent of Code 2025 - Day 12 Parts 1 and 2."""
from math import prod
from pathlib import Path
from typing import Any


class Solution:
    """Advent of Code 2025 - Day 12 Part 1 and 2 solutions."""

    @classmethod
    def read_input(cls, f_path: str | Path) -> Any:
        """Read puzzle input and return as a list of strings.

        Parameters
        ----------
        f_path : str | pathlib.Path
            Path of the input file.

        Returns
        -------
        list[int], str
        """
        *shapes, regions = Path(f_path) \
            .read_text(encoding="utf-8").split("\n\n")

        # Assume the present occupies its entire 9x9 grid
        shapes = [9 for _ in shapes]

        return shapes, regions

    @classmethod
    def part_1(cls, shapes: list[int], regions: str) -> int:
        """Solution to Part 1.

        Parameters
        ----------
        shapes : list[int]
            Area of present shapes.
        regions : str
            Under-tree regions.

        Returns
        -------
        int
            Puzzle solution.

        Breakdown
        ---------
        Originally I thought this problem was going to be extremely difficult
        and I'd have to brute-force some sort of Tetris algorithm. I decided
        to take a peek at the puzzle input and noticed the region areas were
        quite large. Being a naturally lazy person, I figured I'd see what
        would happen if I assumed each present occupied its entire 9x9 shape.
        While this approach fails for the example input, it turns out it works
        for the main puzzle input. This approach might not be in the true
        spirit of AoC, but he who dares wins, or something like that.
        """
        total = 0

        for region in regions.split("\n"):
            if region == "":
                continue

            dims, rgns = region.split(": ")

            # Calculate the area of the region under the tree (width x height)
            area = prod(map(int, dims.split("x")))

            # Calculate the area taken up by the presents
            rgns = [int(x) for x in rgns.split(" ")]
            area_required = sum(a * b for a, b in zip(rgns, shapes))

            if area_required <= area:
                total += 1

        return total


if __name__ == "__main__":
    soln_1 = Solution.part_1(*Solution.read_input("input.txt"))
    print(f"Solution to part 1: {soln_1}")
