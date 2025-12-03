import argparse
from pathlib import Path


TEMPLATE = '''
"""Advent of Code 2025 - Day {day_number} Parts 1 and 2"""
from pathlib import Path

class Solution:

    @classmethod
    def read_input(cls, f_path: str | Path) -> list[str]:
        """Read puzzle input and return as a list of strings."""
        return Path(f_path).read_text(encoding="utf-8").split()

    @classmethod
    def part_1(cls, inp: list[str]) -> int:
        """Solution to Part 1."""
        return 0

    @classmethod
    def part_2(cls, inp: list[str]) -> int:
        """Solution to Part 2."""
        return 0


if __name__ == "__main__":
    input_fname = "input.txt"
    input = Solution.read_input(input_fname)

    soln_1 = Solution.part_1(input)
    soln_2 = Solution.part_2(input)
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


def create_solution_file(root_dir: Path, day_num: str) -> Path:
    """Create the solution file."""
    day_dir = root_dir / day_num
    day_dir.mkdir(exist_ok=True, parents=True)

    f_path = day_dir / "solution.py"

    with open(f_path, "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(day_number=day_num))

    return f_path


if __name__ == "__main__":
    root_dir = Path(".")
    args = parse_args()

    create_solution_file(root_dir, args.day_num)
