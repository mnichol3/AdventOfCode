"""Advent of Code 2025 - Day 11 Parts 1 and 2."""
import re
from functools import lru_cache
from pathlib import Path


def dfs(start: str, end: str) -> list[list[str]]:
    """Find all paths from `start` to `end`.

    Parameters
    ----------
    start : str
        Start node.
    end : str
        End/goal node.

    Returns
    -------
    list[list[str]]
        All paths from `start` to `end`.
    """
    paths = []
    stack = [(start, [start])]

    while stack:
        curr_node, path = stack.pop()

        if curr_node == end:
            paths.append(path)
            continue

        for neighbor in graph.get(curr_node, []):
            if neighbor not in path:
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))

    return paths


@lru_cache(maxsize=512)
def count_paths(curr_node: str, tgt_node: str) -> int:
    """Count the paths from the current node to the target node.

    Recursive depth-first search with memoization.

    Parameters
    ----------
    curr_node : str
        Current node.
    tgt_node : str
        Target/goal node.

    Returns
    -------
    int
        Number of paths from the current node to the target node.
    """
    if curr_node == tgt_node:
        return 1

    if curr_node == "out":
        return 0

    total = 0
    for neighbor in graph[curr_node]:
        total += count_paths(neighbor, tgt_node)

    return total


class Solution:
    """Advent of Code 2025 - Day 11 Part 1 and 2 solutions."""

    @classmethod
    def read_input(cls, f_path: str | Path) -> dict:
        """Read puzzle input.

        Parameters
        ----------
        f_path : str | pathlib.Path
            Path of the input file.

        Returns
        -------
        dict
            Adjacency matrix.
        """
        pattern = re.compile(r"(\w{3})")

        parts = [
            pattern.findall(x)
            for x in Path(f_path).read_text(encoding="utf-8").split("\n")
            if x]

        return {x[0]: x[1:] for x in parts}

    @classmethod
    def part_1(cls) -> int:
        """Solution to Part 1.

        Parameters
        ----------
        None.

        Returns
        -------
        int
            Puzzle solution.

        Breakdown
        ---------
        Find all paths from the start node to the end node --> DFS.

        The `count_paths` function from Part 2 can also be used here but I
        wanted to keep this example of iterative DFS.
        """
        return len(dfs("you", "out"))

    @classmethod
    def part_2(cls) -> int:
        """Solution to Part 2.

        Parameters
        ----------
        None.

        Returns
        -------
        int
            Puzzle solution.

        Breakdown
        ---------
        We want to find all paths between "svr" and "out" that contain both
        "dac" and "fft". While we can just run this through our DFS algorithm
        from part 1, this would take a while. We can greatly decrease compute
        time by looking for a series of shorter paths that pass through our
        nodes of interest:
            "svr" -> "dac"      "svr" -> fft"
            "dac" -> "fft"      "fft" -> dac"
            "fft" -> "out"      "dac" -> "out"

        Taking product of the number of paths in each sub-path gives us the
        total number of possible paths.

        Since it quickly became apparent that we are dealing with orders of
        magnitude more paths than in Part 1, we're going to use a recursive
        DFS function with caching to speed things up.
        """
        path1 = (
            count_paths("svr", "dac")
            * count_paths("dac", "fft")
            * count_paths("fft", "out"))

        path2 = (
            count_paths("svr", "fft")
            * count_paths("fft", "dac")
            * count_paths("dac", "out"))

        return path1 + path2


if __name__ == "__main__":
    graph = Solution.read_input("input.txt")

    soln_1 = Solution.part_1()
    print(f"Solution to part 1: {soln_1}")

    soln_2 = Solution.part_2()
    print(f"Solution to part 2: {soln_2}")
