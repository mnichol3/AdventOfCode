import argparse
from pathlib import Path


TEMPLATE = '''"""Advent of Code 2025 - Day {day_number} Parts 1 and 2."""
from pathlib import Path


class Solution:
    """Advent of Code 2025 - Day {day_number} Part 1 and 2 solutions."""

    @classmethod
    def read_input(cls, f_path: str | Path) -> list[str]:
        """Read puzzle input and return as a list of strings.

        Parameters
        ----------
        f_path : str | pathlib.Path
            Path of the input file.

        Returns
        -------
        list[str]
        """
        return Path(f_path).read_text(encoding="utf-8").split()

    @classmethod
    def part_1(cls, inp: list[str]) -> int:
        """Solution to Part 1.

        Parameters
        ----------
        inp : list[str]
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

    @classmethod
    def part_2(cls, inp: list[str]) -> int:
        """Solution to Part 2.

        Parameters
        ----------
        inp : list[str]
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
    print(f"Solution to part 1: {{soln_1}}")

    soln_2 = Solution.part_2(input)
    print(f"Solution to part 2: {{soln_2}}")

'''


def parse_args() -> argparse.Namespace:
    """Parse and return command line arguments."""
    def padded_num(n: str) -> str:
        return n.zfill(2)

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "day_num",
        type=padded_num,
        help="Advent calendar day number.",
    )

    return parser.parse_args()


if __name__ == "__main__":
    root_dir = Path(".")
    args = parse_args()
    day_num = args.day_num

    day_dir = root_dir / day_num
    day_dir.mkdir(exist_ok=True, parents=True)

    f_path = day_dir / "solution.py"

    with open(f_path, "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(day_number=day_num))
