"""Tests for Day 20 Parts 1 & 2.

Usage
-----
python -m unittest test.py
"""
import unittest

import p1
import p2


class TestPart1(unittest.TestCase):
    """Test cases for Day 20 Part 1"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.maze = p1.Maze(p1.parse_input('example.txt'))
        cls.best_path = cls.maze.bfs()

    def test_best_length(self) -> None:
        """Maze.bfs() returns the expected best path length."""
        self.assertEqual((len(self.best_path))-1, 84)

    def test_cheats(self) -> None:
        """Correct cheats are computed."""
        cheats = p1.find_shortcuts(self.maze, self.best_path)

        self.assertEqual(
            sorted(list(cheats.keys())),
            [2, 4, 6, 8, 10, 12, 20, 36, 38, 40, 64]
        )

        self.assertEqual(cheats[2], 14)
        self.assertEqual(cheats[4], 14)
        self.assertEqual(cheats[6], 2)
        self.assertEqual(cheats[8], 4)
        self.assertEqual(cheats[10], 2)
        self.assertEqual(cheats[12], 3)
        self.assertEqual(cheats[20], 1)
        self.assertEqual(cheats[36], 1)
        self.assertEqual(cheats[38], 1)
        self.assertEqual(cheats[40], 1)
        self.assertEqual(cheats[64], 1)


class TestPart2(unittest.TestCase):
    """Test cases for Day 20 Part 2"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.maze = p1.Maze(p1.parse_input('example.txt'))
        cls.best_path = cls.maze.bfs()

    def test_best_length(self) -> None:
        """Maze.bfs() returns the expected best path length."""
        self.assertEqual((len(self.best_path))-1, 84)

    def test_cheats(self) -> None:
        """Correct cheats are computed."""
        cheats = p2.find_shortcuts(self.maze, self.best_path, length=20)

        self.assertEqual(
            sorted(list(cheats.keys())),
            [50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76]
        )

        self.assertEqual(cheats[50], 32)
        self.assertEqual(cheats[52], 31)
        self.assertEqual(cheats[54], 29)
        self.assertEqual(cheats[56], 39)
        self.assertEqual(cheats[58], 25)
        self.assertEqual(cheats[60], 23)
        self.assertEqual(cheats[62], 20)
        self.assertEqual(cheats[64], 19)
        self.assertEqual(cheats[66], 12)
        self.assertEqual(cheats[68], 14)
        self.assertEqual(cheats[70], 12)
        self.assertEqual(cheats[72], 22)
        self.assertEqual(cheats[74], 4)
        self.assertEqual(cheats[76], 3)


if __name__ == '__main__':
    unittest.main()