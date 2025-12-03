"""Advent of Code 2025 - Day 03 Parts 1 and 2"""
from pathlib import Path


class Solution:

    @classmethod
    def read_input(cls, f_path: str | Path) -> list[str]:
        """Read and parse the puzzle input."""
        return Path(f_path).read_text(encoding="utf-8").split()

    @classmethod
    def part_1(cls, banks: list[str]) -> None:
        """Solution to Part 1."""
        joltages = []

        for bank in banks:
            curr_joltage = 0
            max_joltage = -10e10

            for i in range(len(bank) - 1):
                for j in range(i + 1, len(bank)):
                    curr_joltage = int(f"{bank[i]}{bank[j]}")
                    max_joltage = max(max_joltage, curr_joltage)

            joltages.append(max_joltage)

        print(f"The solution for Part 1 is {sum(joltages)}")



if __name__ == "__main__":
    input = Solution.read_input(Path("input.txt"))
    Solution.part_1(input)
