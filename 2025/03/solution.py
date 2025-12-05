"""Advent of Code 2025 - Day 03 Parts 1 and 2"""
from pathlib import Path


class Solution:

    @classmethod
    def read_input(cls, f_path: str | Path) -> list[str]:
        """Read and parse the puzzle input."""
        return Path(f_path).read_text(encoding="utf-8").split()

    @classmethod
    def part_1(cls, banks: list[str]) -> int:
        """Solution to Part 1."""
        joltages = []

        for bank in banks:
            curr_joltage = 0
            max_joltage = -1

            for i in range(len(bank) - 1):
                for j in range(i + 1, len(bank)):
                    curr_joltage = int(f"{bank[i]}{bank[j]}")
                    max_joltage = max(max_joltage, curr_joltage)

            joltages.append(max_joltage)

        return sum(joltages)

    @classmethod
    def part_2(cls, inp: list[str]) -> int:
        """Greedy solution to Part 2."""
        joltages = []
        bank_len = len(inp[0])
        joltage_len = 12

        for bank in inp:
            max_joltage = []
            start_idx = 0

            for pos in range(joltage_len):
                remaining = joltage_len - pos - 1
                max_idx = bank_len - remaining
                max_val = max(bank[start_idx:max_idx])

                for i in range(start_idx, max_idx):
                    if bank[i] == max_val:
                        max_joltage.append(max_val)
                        start_idx = i + 1
                        break

            joltages.append(int("".join(max_joltage)))

        return sum(joltages)


if __name__ == "__main__":
    input = Solution.read_input(Path("input.txt"))
    print(f"The solution for Part 1 is {Solution.part_1(input)}")
    print(f"The solution for Part 2 is {Solution.part_2(input)}")
