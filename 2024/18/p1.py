"""Advent of Code 2024 - Day 18 Parts 1 & 2"""
from collections import deque
from enum import Enum
from pathlib import Path


Point = tuple[int, int]


def parse_input(f_path: str = 'input.txt') -> list[Point]:
    """Return input from a file and return as a list of tuples.

    Parameters
    ----------
    f_path: str, optional
        Path of the input file to read. Default is 'input.txt'.

    Returns
    -------
    list of tuple of (int, int)
        List of (i, j) coordinates of maze obstructions.
    """
    return [
        tuple(map(int, x.split(',')))[::-1]
        for x in Path(f_path).read_text().split('\n') if x
    ]


class Move(Enum):
    """Maze movements, represented by their delta i and delta j values."""
    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)


class MemoryMap:
    """Class representing a 2-D maze.

    Attributes
    ----------
    bytes: list of (int, int)
        Indices of maze obstructions.
    ni: int
        Size of the maze in the i-direction.
    nj: int
        Size of the maze in the j-direction.
    map: list of list of str
        The maze, where '#' are obstructions and '.' are open spaces.
    """

    def __init__(
        self,
        bytes: list[Point],
        ni: int = 71,
        nj: int = 71,
        add_bytes: int = 1024,
    ) -> None:
        """Instantiate a new MemoryMap instance.

        Parameters
        ----------
        bytes: list of (int, int)
            Indices of maze obstructions.
        ni: int, optional
            Size of the maze in the i-direction. Default is 71.
        nj: int
            Size of the maze in the j-direction. Default is 71.
        add_bytes: int
            Number of obstructions to place into the maze. Default is 1024.
        """
        self.bytes = bytes
        self.byte_idx = add_bytes - 1
        self.ni = ni
        self.nj = nj
        self.map = [['.'] * self.nj for _ in range(self.ni)]
        self._corrupt(add_bytes)

    def _corrupt(self, num_bytes: int) -> None:
        """Place maze obstructions.

        Parameters
        ----------
        num_bytes: int
            Number of obstructions to place.

        Returns
        -------
        None.
        """
        for (i, j) in self.bytes[:num_bytes]:
            self.map[i][j] = '#'

    def _valid_move(
        self,
        curr_pos: Point,
        move: Point,
    ) -> Point | None:
        """Determine if the given move is valid. If it is, return the
        coordinates of the resulting grid space. Else return None.

        Parameters
        ----------
        curr_pos: tuple of (int, int)
            i and j coordinates of the current position.
        move: tuple of (int, int)
            Delta i and Delta values representing the move.

        Returns
        -------
        None
            The move is out of bounds.
        tuple of (int, int) or None
            i and j coordinates of the resulting move if valid.
        """
        i, j = curr_pos
        ii = i + move[0]
        jj = j + move[1]

        if 0 <= ii < self.ni and 0 <= jj < self.nj and self.map[ii][jj] != '#':
            return (ii, jj)

        return None

    def add_byte(self) -> None:
        self.byte_idx += 1
        i, j = self.bytes[self.byte_idx]
        self.map[i][j] = '#'

    def solve(
        self,
        start_pos: Point = (0, 0),
        end_pos: Point = None,
    ) -> list[Point]:
        """BFS returning the shortest path.

        Parameters
        ----------
        start_pos: tuple of (int, int), optional
            Starting position. Default is (0, 0).
        end_pos: tuple of (int, int), optional
            End position/goal. Default is (self.ni - 1, self.nj - 1)
        part: int, optional
            Indicates whether we are solving part 1 or 2 of the problem.
            Default is 1.

        Returns
        -------
        list of tuple of (int, int)
            Shortest path between the start and end points.
        """
        end_pos = (self.ni-1, self.nj-1) if end_pos is None else end_pos

        visited = {}
        queue = deque()

        visited[start_pos] = None
        queue.append(start_pos)

        while queue:
            curr_pos = queue.popleft()

            if curr_pos == end_pos:
                path = []
                while curr_pos:
                    path.append(curr_pos)
                    curr_pos = visited[curr_pos]
                return path[::-1]

            for move in Move:
                neighbor = self._valid_move(curr_pos, move.value)
                if neighbor is not None and neighbor not in visited:
                    visited[neighbor] = curr_pos
                    queue.append(neighbor)

        # Reverse since answer is in (x, y)
        return self.bytes[self.byte_idx][::-1]


    def print(self, path: list[Point] = None) -> None:
        """Print the maze.

        Parameters
        ----------
        path: list of tuple of (int, int), optional
            Path connecting the starting point to end point.

        Returns
        -------
        None.
        """
        if path:
            for (i, j) in path:
                self.map[i][j] = 'O'

        for i in range(self.ni):
            print(''.join(self.map[i]))

    def __repr__(self) -> str:
        """Return a string representation of the class."""
        return f'<{self.__class__.__name__} ni={self.ni}, nj={self.nj}>'


if __name__ == '__main__':
    mem = MemoryMap(parse_input())

    part1 = mem.solve()
    print(f'Part 1 Answer: {len(part1)-1}')

    part2 = mem.solve()[-1]
    while part2 == (70, 70):
        mem.add_byte()
        part2 = mem.solve()

        if len(part2) > 2:
            part2 = part2[-1]

    print(f'Part 2 Answer: {part2}')
