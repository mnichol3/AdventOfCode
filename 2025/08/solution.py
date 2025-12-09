"""Advent of Code 2025 - Day 8 Parts 1 and 2"""
from math import sqrt
from pathlib import Path


# Type alias
XYZ = tuple[int, int, int]


class UnionFind:
    """A simple disjoint-set/union-find data structure."""

    def __init__(self):
        """Instantiate a new UnionFind."""
        self.parent: dict[int, int] = {}

    def make_set(self, elements: list[XYZ]) -> None:
        """Add elements to the parent set.

        Parameters
        ----------
        elements : list[XYZ]
            List of elements to add.
        """
        for ele in elements:
            self.parent[ele] = ele

    def find(self, element: XYZ) -> XYZ:
        """Find an element in the set.

        Parameters
        ----------
        element : XYZ
            Element to find.
        """
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])

        return self.parent[element]

    def union(self, element1: XYZ, element2: XYZ) -> None:
        """Unionize two elements.

        Parameters
        ----------
        element1 : XYZ
            First element.
        elemtn2 : XYZ
            Second element.
        """
        root1 = self.find(element1)
        root2 = self.find(element2)

        if root1 != root2:
            self.parent[root1] = root2


class Solution:
    """Advent of Code 2025 - Day 8 Part 1 and 2 solutions"""

    def __init__(self, input_path: Path):
        """Instantiate a new Solution object.

        Parameters
        ----------
        input_path : Path
            Path of the puzzle input file.
        """
        self.input = self.read_input(input_path)
        self.n = len(self.input)
        self.dists = sorted(self.get_dists(self.input))

    @classmethod
    def read_input(cls, f_path: str | Path) -> list[XYZ]:
        """Read puzzle input and return as a list of strings.

        Parameters
        ----------
        f_path : str | pathlib.Path
            Path of the input file.

        Returns
        -------
        list[XYZ]
        """
        return [
            tuple(map(int, x.split(",")))
            for x in Path(f_path).read_text(encoding="utf-8").split()]

    def part_1(self, n_connections: int = 1000) -> int:
        """Solution to Part 1.

        Parameters
        ----------
        n_connections : int, default 1000
            Number of connections to create. Default is 1000.

        Returns
        -------
        int
            Puzzle solution.

        Breakdown
        ---------
        Since we want to group the (x, y, z) coordinates into discrete groups,
        I decided that a disjoint-set/union-find data structure would be the
        best fit here. We don't actually care whats in each set, we only care
        about the size of the sets and if an element has been added to a set
        or not. Because of this, our union-find data structure can be
        implemented as a dictionary containing connecting a single element
        to a single set-mate.

        The general workflow is as follows:
            1. Compute the distances between all points, then sort.
            2. Iterate over the 1000 closest distances and create 2-element
               circuits by union-ing their coordinates.
            3. Create a dictionary to store the number of times a coordinate
               appears in the circuits created in step 2.
            4. Sort the count values and take the product of the 3 largest
               counts.
        """
        union_find = UnionFind()
        union_find.make_set(list(range(self.n)))

        for idx in range(min(n_connections, len(self.dists))):
            _, i, j = self.dists[idx]
            union_find.union(i, j)

        parents = dict.fromkeys(list(range(self.n)), 0)

        for i in range(self.n):
            j = union_find.find(i)
            parents[j] += 1

        k = sorted(parents.values())

        return k[-3] * k[-2] * k[-1]

    def part_2(self) -> int:
        """Solution to Part 2.

        Returns
        -------
        int
            Puzzle solution.

        Breakdown
        ---------
        We want to continue combining coordinates until they're all in one
        large group. Based on the framework created for Part 1, this means
        we want to continue to union coordinates until all values of the
        union-find parent dictionary are equal. Then, as the problem states,
        simply return the x-coordinates of the final two connected coordinates.
        """
        union_find = UnionFind()
        union_find.make_set(list(range(self.n)))

        for dist in self.dists:
            _, i, j = dist
            union_find.union(i, j)

            if all(
                union_find.find(i) == union_find.find(0)
                for i in range(self.n)
            ):
                return self.input[i][0] * self.input[j][0]

        return -1

    @classmethod
    def get_dists(cls, elements: list[XYZ]) -> list[float]:
        """Compute the Euclidean distances between all elements.

        Parameters
        ----------
        elements : list[XYZ]
            List of (x, y, z) points.

        Returns
        -------
        list[float]
            Euclidean distances between points.
        """
        def calc_dist(a: XYZ, b: XYZ) -> float:
            """Calculate the Euclidean distance between point a and point b."""
            return sqrt(sum((a[i] - b[i])**2 for i in range(3)))

        n = len(elements)
        dists = []

        for i in range(n):
            for j in range(i + 1, n):
                dists.append((calc_dist(elements[i], elements[j]), i, j))

        return dists


def test():
    """Simple solution tests using example input."""
    solution = Solution("example.txt")

    assert solution.part_1(n_connections=10) == 40
    assert solution.part_2() == 25272

    print("Both tests passed!")


def run():
    """Run solutions with puzzle input."""
    solution = Solution("input.txt")

    soln_1 = solution.part_1()
    print(f"Solution to part 1: {soln_1}")

    soln_2 = solution.part_2()
    print(f"Solution to part 2: {soln_2}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r"
        "--run-mode",
        dest="run_mode",
        type=str,
        choices=["run", "test"],
        default="run",
    )

    args = parser.parse_args()

    if args.run_mode == "run":
        run()
    else:
        test()
