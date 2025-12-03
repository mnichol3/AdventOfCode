"""Advent of Code 2025 - Day 02 Parts 1 and 2"""
from pathlib import Path


class Solution:

    @classmethod
    def read_input(cls, f_path: str | Path) -> list[str]:
        """Read and parse the puzzle input."""
        return Path(f_path).read_text(encoding="utf-8").split(",")

    @classmethod
    def part_1(cls, product_ids: list[str]) -> None:
        """Solution to Part 1."""
        num_invalid = 0

        for id in product_ids:
            first_id, last_id = map(int, id.split("-"))

            for curr_id in range(first_id, last_id+1):
                str_id = str(curr_id)
                midpoint = len(str_id) // 2

                if (
                    str_id.startswith(str_id[midpoint:])
                    and len(str_id) % 2 == 0
                ):
                    num_invalid += curr_id

        print(f"The solution for Part 1 is {num_invalid}")

    @classmethod
    def part_2(cls, product_ids: list[str]) -> None:
        """Solution to Part 2."""
        invalid = []

        for id in product_ids:
            first_id, last_id = map(int, id.split("-"))

            for curr_id in range(first_id, last_id+1):
                str_id = str(curr_id)

                for pattern_len in range(1, len(str_id) // 2 + 1):
                    if len(str_id) % pattern_len != 0:
                        continue

                    num_reps = len(str_id) // pattern_len
                    pattern = str_id[:pattern_len]

                    if pattern * num_reps == str_id and curr_id not in invalid:
                        invalid.append(curr_id)

        print(f"The solution for Part 2 is {sum(invalid)}")


if __name__ == "__main__":
    input = Solution.read_input(Path("input.txt"))
    Solution.part_1(input)
    Solution.part_2(input)
