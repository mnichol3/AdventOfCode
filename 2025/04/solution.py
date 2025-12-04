"""Advent of Code 2025 - Day 04 Parts 1 and 2"""
from pathlib import Path


class Solution:

    window_size = 3
    half_window = window_size // 2

    @classmethod
    def read_input(cls, f_path: str | Path) -> list[list[str]]:
        """Read puzzle input and return as a list of strings."""
        return [
            list(x) for x in Path(f_path).read_text(encoding="utf-8").split()
            if x]

    @classmethod
    def part_1(cls, inp: list[str]) -> int:
        """Solution to Part 1."""
        result = 0
        n_rows = len(inp)
        n_cols = len(inp[0])

        for row in range(n_rows):
            for col in range(n_cols):
                curr_window = []

                for i in range(
                    row - cls.half_window,
                    row - cls.half_window + cls.window_size
                ):
                    row_vals = []

                    for j in range(
                        col - cls.half_window,
                        col - cls.half_window + cls.window_size
                    ):

                        if i < 0 or j < 0:
                            row_vals.append(".")
                            continue

                        try:
                            row_vals.append(inp[i][j])
                        except IndexError:
                            row_vals.append(".")

                    curr_window.append(row_vals)

                num_neighbors = sum(x.count("@") for x in curr_window)
                if curr_window[1][1] == "@" and num_neighbors < 5:
                    result += 1

        return result

    @classmethod
    def part_2(cls, inp: list[str]) -> int:
        """Solution to Part 2.."""
        result = 0
        num_removed = -1
        n_rows = len(inp)
        n_cols = len(inp[0])

        while num_removed != 0:
            num_removed = 0

            for row in range(n_rows):
                for col in range(n_cols):
                    curr_window = []

                    for i in range(
                        row - cls.half_window,
                        row - cls.half_window + cls.window_size
                    ):
                        row_vals = []

                        for j in range(
                            col - cls.half_window,
                            col - cls.half_window + cls.window_size
                        ):

                            if i < 0 or j < 0:
                                row_vals.append(".")
                                continue

                            try:
                                row_vals.append(inp[i][j])
                            except IndexError:
                                row_vals.append(".")

                        curr_window.append(row_vals)

                    num_neighbors = sum(x.count("@") for x in curr_window)
                    if curr_window[1][1] == "@" and num_neighbors < 5:
                        inp[row][col] = "."
                        num_removed = 1
                        result += 1

        return result


if __name__ == "__main__":
    input = Solution.read_input(Path("input.txt"))

    soln_1 = Solution.part_1(input)
    print(f"The solution for Part 1 is {soln_1}")

    soln_2 = Solution.part_2(input)
    print(f"The solution for Part 2 is {soln_2}")
