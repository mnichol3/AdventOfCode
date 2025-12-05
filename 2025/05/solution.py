"""Advent of Code 2025 - Day 5 Parts 1 and 2"""
from pathlib import Path


class Solution:
    """Advent of Code 2025 - Day 5 Part 1 and 2 solutions"""

    @classmethod
    def read_input(
        cls,
        f_path: str | Path,
    ) -> tuple[list[tuple[int, int]], list[int]]:
        """Read puzzle input.

        Parameters
        ----------
        f_path : str | pathlib.Path
            Path of the input file to read.

        Returns
        -------
        list[tuple[int, int]
            ID start and end values.
        list[int]
            IDs.
        """
        raw_inp = Path(f_path).read_text(encoding="utf-8").split()

        # Search for the end of the ID range portion of the input
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
    def part_1(cls, ranges: list[tuple[int, int]], ids: list[int]) -> int:
        """Solution to Part 1.

        Parameters
        ----------
        ranges : list[tuple[int, int]]
            Beginning and end values of valid ID ranges.
        ids : list[int]
            IDs to test.

        Returns
        -------
        int
            Number of valid IDs.

        Breakdown
        ---------
        We need to identify all IDs that fall into any of the given ID ranges.
        Since we only want to count an ID once regardless of how many ID
        ranges it is contained by, all IDs deemed valid for a given range
        will be added to a set. Taking the length of the set yields the
        number of valid IDs.
        """
        fresh = set()

        for (min_id, max_id) in ranges:
            for curr_id in ids:
                if min_id <= curr_id <= max_id:
                    fresh.add(curr_id)

        return len(fresh)

    @classmethod
    def part_2(cls, ranges: list[tuple[int, int]]) -> int:
        """Solution to Part 2.

        Parameters
        ----------
        ranges : list[tuple[int, int]]
            Beginning and end values of valid ID ranges.

        Returns
        -------
        int
            Sum of the sizes of all ID ranges.

        Breakdown
        ---------
        The idea here is to combine as many adjacent/overlapping ID ranges as
        we can, then sum the sizes of the ranges.

        Attempting to solve this part with an approach similar to Part 1 will
        lead to memory errors due to the size of the integers in the puzzle
        input.
        """
        merged_ranges = []
        ranges.sort()

        for (min_id, max_id) in ranges:
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
    id_ranges, id_list = Solution.read_input(input_fname)

    soln_1 = Solution.part_1(id_ranges, id_list)
    print(f"Solution to part 1: {soln_1}")

    soln_2 = Solution.part_2(id_ranges)
    print(f"Solution to part 2: {soln_2}")
