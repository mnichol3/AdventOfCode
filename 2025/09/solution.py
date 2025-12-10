"""Advent of Code 2025 - Day 09 Parts 1 and 2."""
import math
from pathlib import Path
from typing import Any

from shapely import Polygon
from shapely.prepared import prep


def calc_area(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    """Compute the area of a rectangle formed by two corners."""
    x1, y1 = point1
    x2, y2 = point2

    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


class Solution:
    """Advent of Code 2025 - Day 09 Part 1 and 2 solutions."""

    @classmethod
    def read_input(cls, f_path: str | Path) -> Any:
        """Read puzzle input and return as a list of strings.

        Parameters
        ----------
        f_path : str | pathlib.Path
            Path of the input file.

        Returns
        -------
        list[tuple[int, ...]]
        """
        return [
            tuple(map(int, x.split(",")))
            for x in Path(f_path).read_text(encoding="utf-8").split()]

    @classmethod
    def part_1(cls, inp: list[tuple[int, int]]) -> int:
        """Solution to Part 1.

        Parameters
        ----------
        inp: list[tuple[int, ...]]
            Puzzle input.

        Returns
        -------
        int
            Puzzle solution.

        Breakdown
        ---------
        Pretty straight-forward. Iterate over every combination of coordinates,
        treating them as vertices, and compute the area of the rectangle they
        create.
        """
        n = len(inp)
        max_area = -1

        for i in range(n):
            for j in range(i + 1, n):
                max_area = max(max_area, calc_area(inp[i], inp[j]))

        return max_area

    @classmethod
    def part_2(cls, inp: list[tuple[int, int]]) -> int:
        """Solution to Part 2.

        Parameters
        ----------
        inp: list[str]
            Puzzle input.

        Returns
        -------
        int
            Puzzle solution.

        Breakdown
        ---------
        Ok, so I was stumped on this one and resorted to using the shapely
        library. Equipped with those tools, this part became relatively simple.
        Similarly to Part 1, we iterate over each pair of potential vertices.
        The only difference is that the area of a rectangle is only considered
        for comparison to the max area if e a shapely.Polygon created from the
        vertices is contained by the larger polygon formed by the red & green
        tiles.
        """
        def radial_sort(
            vertices: list[tuple[int, int]],
        ) -> list[tuple[int, int]]:
            """Sort vertices in counter-clockwise order around the centroid."""
            def sort_key(point):
                return math.atan2(point[1] - center[1], point[0] - center[0])

            center_x = sum(p[0] for p in vertices) / len(vertices)
            center_y = sum(p[1] for p in vertices) / len(vertices)
            center = (center_x, center_y)

            return sorted(vertices, key=sort_key)

        n = len(inp)
        max_area = 0

        # Prep the polygon to improve performance
        main_polygon = prep(Polygon(inp))

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = inp[i]
                x2, y2 = inp[j]

                curr_area = calc_area(inp[i], inp[j])
                if curr_area <= max_area:
                    continue

                # Sort vertices so no edges intersect
                curr_poly = Polygon(
                    radial_sort([inp[i], inp[j], (x1, y2), (x2, y1)]))

                if main_polygon.contains(curr_poly):
                    max_area = curr_area

        return max_area


if __name__ == "__main__":
    input_fname = "input.txt"
    input = Solution.read_input(input_fname)

    soln_1 = Solution.part_1(input)
    print(f"The solution for Part 1 is {soln_1}")

    soln_2 = Solution.part_2(input)
    print(f"The solution for Part 2 is {soln_2}")
