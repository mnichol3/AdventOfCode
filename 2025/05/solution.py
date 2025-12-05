"""Advent of Code 2025 - Day 5 Parts 1 and 2"""
from pathlib import Path


class Solution:

    @classmethod
    def read_input(
        cls,
        f_path: str | Path,
    ) -> tuple[list[tuple[int, int]], list[int]]:
        """Read puzzle input.

        Returns
        -------
        list[tuple[int, int]
            ID start and end values.
        list[int]
            IDs.
        """
        raw_inp = Path(f_path).read_text(encoding="utf-8").split()

        i = 1
        curr_val = raw_inp[i]
        while "-" in curr_val:
            i += 1
            curr_val = raw_inp[i]

        ranges = []
        for line in raw_inp[:i]:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))

        return ranges, [int(x) for x in raw_inp[i:]]

    @classmethod
    def part_1(cls, id_ranges: list[tuple[int, int]], ids: list[int]) -> int:
        """Solution to Part 1."""
        # Use a set to avoid double-counting IDs that are contained by 2 or
        # more ranges
        fresh = set()

        for (min_id, max_id) in id_ranges:
            for curr_id in ids:
                if min_id <= curr_id <= max_id:
                    fresh.add(curr_id)

        return len(fresh)

    @classmethod
    def part_2(cls, id_ranges: list[tuple[int, int]]) -> int:
        """Solution to Part 2.

        The idea here is to combine as many adjacent/overlapping ID ranges as
        we can, then sum the sizes of each range.

        Attempting to solve this part the an approach similar to Part 1 will
        lead to memory errors due to the size of the integers in the puzzle
        input.
        """
        merged_ranges = []
        id_ranges.sort()

        for (min_id, max_id) in id_ranges:
            if merged_ranges and min_id <= merged_ranges[-1][1] + 1:
                # Overlapping or adjacent - extend the last range
                merged_ranges[-1] = (
                    merged_ranges[-1][0], max(merged_ranges[-1][1], max_id))
            else:
                # Non-overlapping - add as new range
                merged_ranges.append((min_id, max_id))

        total = 0
        for start, end in merged_ranges:
            total += (end - start + 1)

        return total


if __name__ == "__main__":
    input_fname = "input.txt"
    id_ranges, ids = Solution.read_input(input_fname)

    soln_1 = Solution.part_1(id_ranges, ids)
    print(f"Solution to part 1: {soln_1}")

    soln_2 = Solution.part_2(id_ranges)
    print(f"Solution to part 2: {soln_2}")
