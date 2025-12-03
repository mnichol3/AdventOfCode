"""Advent of Code 2025 - Day 01 Parts 1 and 2"""
from math import floor
from operator import add, sub
from pathlib import Path


class Solution:

    rotation = {
        "L": sub,
        "R": add,
    }

    @classmethod
    def read_input(cls, f_path: str | Path) -> list[str]:
        """Read and parse the puzzle input."""
        return Path(f_path).read_text(encoding="utf-8").split()

    @classmethod
    def part_1(cls, instructions: list[str]) -> None:
        """Solution to Part 1."""
        password = 0
        curr_pos = 50

        for instr in instructions:
            curr_pos = cls.rotation[instr[0]](curr_pos, int(instr[1:])) % 100

            if curr_pos == 0:
                password += 1

        print(f"The password for Part 1 is {password}")

    @classmethod
    def part_2(cls, instructions: list[str]) -> None:
        """Solution to Part 2."""
        raise NotImplementedError("TODO: make this work lol")
        password = 0
        curr_pos = 50
        prev_pos = None

        for instr in instructions:
            zero_crossings = 0

            prev_pos = curr_pos
            curr_pos = cls.rotation[instr[0]](curr_pos, int(instr[1:]))

            if not 0 <= curr_pos <= 99:
                zero_crossings = abs(floor(curr_pos / 100))
                curr_pos = curr_pos % 100
                if zero_crossings and (curr_pos == 0 or prev_pos == 0):
                    zero_crossings -= 1

                password += zero_crossings

            if curr_pos == 0:
                password += 1

        print(f"The password for Part 2 is {password}")

    @classmethod
    def part_2_brute(cls, instructions: list[str]) -> None:
        """Yeah we're really doing this on Day 1."""
        password = 0
        curr_pos = 50
        prev_pos = None

        for instr in instructions:
            spin_dir = instr[0]
            spin_func = cls.rotation[spin_dir]
            crossed_zero = False
            prev_pos = cls.rotation[
                "L" if spin_dir == "R" else "R"](curr_pos, 1) % 100

            for n in range(int(instr[1:])):
                curr_pos = spin_func(curr_pos, 1) % 100
                print(f"{curr_pos=}, {prev_pos=}")

                if (
                    spin_dir == "R" and curr_pos == 1 and prev_pos == 99
                    and n != 0
                ) or (
                    spin_dir == "L" and curr_pos == 99 and prev_pos == 1
                    and n != 0
                ):
                    password += 1
                    crossed_zero = True

                prev_pos = spin_func(prev_pos, 1) % 100

            if curr_pos == 0:
                password += 1

        print(f"The password for Part 2 is {password}")


if __name__ == "__main__":
    puzzle_input = Solution.read_input(Path("input.txt"))

    Solution.part_1(puzzle_input)
    Solution.part_2_brute(puzzle_input)
