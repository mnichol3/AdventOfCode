
"""Advent of Code 2025 - Day 07 Parts 1 and 2."""
from pathlib import Path


class Solution:
    """Advent of Code 2025 - Day 07 Part 1 and 2 solutions."""

    @classmethod
    def read_input(cls, f_path: str | Path) -> list[list[str]]:
        """Read puzzle input and return as a list of strings.

        Parameters
        ----------
        f_path : str | pathlib.Path
            Path of the input file.

        Returns
        -------
        list[list[str]]
        """
        return [
            list(x) for x in Path(f_path).read_text(encoding="utf-8").split()]

    @classmethod
    def part_1(cls, inp: list[list[str]]) -> int:
        """Solution to Part 1.

        Parameters
        ----------
        inp: list[list[str]]
            Puzzle input.

        Returns
        -------
        int
            Number of tachyon splits.

        Breakdown
        ---------
        TODO
        """
        num_splits = 0
        n_cols = len(inp[0])
        start_pos = inp[0].index("S")

        beams = [" "] * n_cols
        beams[start_pos] = "|"

        for row in inp[1:]:
            for col_idx, col_val in enumerate(row):
                if col_val == "^" and beams[col_idx] == "|":
                    num_splits += 1
                    beams[col_idx] = " "

                    for offset in [-1, 1]:
                        try:
                            beams[col_idx + offset] = "|"
                        except IndexError:
                            pass

        return num_splits

    @classmethod
    def part_2(cls, inp: list[list[str]]) -> int:
        """Solution to Part 2.

        Parameters
        ----------
        inp: list[list[str]]
            Puzzle input.

        Returns
        -------
        int
            Puzzle solution.

        Breakdown
        ---------
        TODO
        """
        return 0


if __name__ == "__main__":
    input_fname = "input.txt"
    input = Solution.read_input(input_fname)

    soln_1 = Solution.part_1(input)
    print(f"The solution for Part 1 is {soln_1}")

    soln_2 = Solution.part_2(input)
    print(f"The solution for Part 2 is {soln_2}")
