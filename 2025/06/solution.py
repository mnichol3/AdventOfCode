"""Advent of Code 2025 - Day 06 Parts 1 and 2."""
import math
import re
from pathlib import Path


class Solution:
    """Advent of Code 2025 - Day 06 Part 1 and 2 solutions."""

    operators = {
        "*": math.prod,
        "+": sum,
    }

    @classmethod
    def read_input(cls, f_path: str | Path) -> list[str]:
        """Read puzzle input and return as a list of strings."""
        return Path(f_path).read_text(encoding="utf-8").splitlines()

    @classmethod
    def part_1(cls, inp: list[str]) -> int:
        """Solution to Part 1.

        Parameters
        ----------
        inp : list[str]
            List of input rows as strings.

        Returns
        -------
        int
            Sum of equations.

        Breakdown
        ---------
        This part is pretty straight-forward. Essentially, we create a 2D list
        containing lists of row values and transpose it in order to group each
        equation into its own list. From there we just determine which math
        operator function we need and pass the list of values to it.
        """
        processed = []
        pattern = re.compile(r"\d+|[+\-*/]")

        for row in inp:
            curr_row = pattern.findall(row)

            if curr_row:
                processed.append(curr_row)

        # Transpose
        processed = [list(row) for row in zip(*processed)]

        result = 0

        for row in processed:
            oper = cls.operators[row[-1]]
            vals = list(map(int, row[:-1]))
            result += oper(vals)

        return result

    @classmethod
    def part_2(cls, inp: list[str]) -> int:
        """Solution to Part 2.

        Parameters
        ----------
        inp : list[str]
            List of input rows as strings.

        Returns
        -------
        int
            Sum of equations.

        Breakdown
        ---------
        This part was a bit trickier than part 1. The logic here is to iterate
        over the columns from right to left in order to construct one equation
        at a time. Since we're moving right to left, we know we've constructed
        a full equation when the final element in the current column is a math
        operator ("*" or "+"). Once we have an equation, its straight forward
        to convert the string lists to integers and pass them to the
        corresponding operator function.
        """
        result = 0

        # Assumes all rows are the same length
        n_rows = len(inp)
        n_cols = len(inp[0])
        col_idx = n_cols - 1

        problem = []
        while col_idx >= 0:
            oper = None

            # Get all values in the current column
            col_vals = [
                inp[i][col_idx]
                for i in range(n_rows) if inp[i][col_idx] != " "]

            try:
                if col_vals[-1] in cls.operators.keys():
                    oper = cls.operators[col_vals[-1]]
                    col_vals = col_vals[:-1]
            except IndexError:
                # Blank column, move on
                pass
            else:
                problem.append(int("".join(col_vals)))

                if oper:
                    result += oper(problem)
                    problem = []

            col_idx -= 1

        return result


if __name__ == "__main__":
    input = Solution.read_input(Path("input.txt"))

    soln_1 = Solution.part_1(input)
    print(f"The solution for Part 1 is {soln_1}")

    soln_2 = Solution.part_2(input)
    print(f"The solution for Part 2 is {soln_2}")
