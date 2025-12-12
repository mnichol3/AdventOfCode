"""Advent of Code 2025 - Day 10 Parts 1 and 2."""
import sys
from collections import deque
from pathlib import Path
from typing import Any

from z3 import Int, Optimize, Sum, sat


class Solution:
    """Advent of Code 2025 - Day 10 Part 1 and 2 solutions."""

    @classmethod
    def read_input(cls, f_path: str | Path) -> Any:
        """Read puzzle input.

        Parameters
        ----------
        f_path : str | pathlib.Path
            Path of the input file.

        Returns
        -------
        List of tuples of:
            - list[bool] : Goal state of the machine.
            - list[bool] : Starting state of the machine (all False/off).
            - list[list[int, ...]] : Button toggles.
            - list[int] : Joltages.
        """
        instructions = []

        lines = Path(f_path).read_text(encoding="utf-8").splitlines()

        for line in lines:
            parts = line.split(" ")

            buttons = [
                [int(x) for x in button.strip("()").split(",")]
                for button in parts[1:-1]]

            goal = [char == "#" for char in parts[0][1:-1]]
            curr_state = [False] * len(goal)

            joltages = [int(x) for x in parts[-1].strip("{}").split(",")]

            instructions.append((goal, curr_state, buttons, joltages))

        return instructions

    @classmethod
    def part_1(cls, inp: Any) -> int:
        """Solution to Part 1.

        Parameters
        ----------
        inp: Any
            List of tuples of:
            - list[bool] : Goal state of the machine.
            - list[bool] : Starting state of the machine (all False/off).
            - list[list[int, ...]] : Button toggles.
            - list[int] : Joltages.

        Returns
        -------
        int
            Puzzle solution.

        Breakdown
        ---------
        We're using breadth-first search to explore how many button presses
        are required to reach our desired machine state, where each "node"
        is a tuple of the current machine state and the number of button
        presses that yielded the machine state.
        """
        total = 0

        for machine in inp:
            goal_state, curr_state, buttons, _ = machine

            # Store both the machine state and number of button presses (depth)
            # in the queue.
            q = deque(((curr_state, 0), ))
            visited = set(str(curr_state))

            while q:
                curr_state, depth = q.popleft()

                if curr_state == goal_state:
                    total += depth
                    break

                for button in buttons:
                    # Apply each button to get a new machine state
                    new_state = curr_state[:]

                    for press in button:
                        # Press the button -> toggle the indicator light
                        new_state[press] = not new_state[press]

                    to_add = new_state

                    if str(to_add) not in visited:
                        visited.add(str(to_add))
                        q.append((to_add, depth + 1))

        return total

    @classmethod
    def part_2(cls, inp: Any) -> int:
        """Solution to Part 2.

        Parameters
        ----------
        inp: Any
            Puzzle input.

        Returns
        -------
        int
            Puzzle solution.

        Breakdown
        ---------
        Linear optimization using the z3 library because I'm lazy.
        """
        goal_states = []
        buttons = []
        joltages = []

        for machine in inp:
            goal_state, _, curr_buttons, curr_joltages = machine
            goal_states.append(goal_state)
            buttons.append(curr_buttons)
            joltages.append(curr_joltages)

        def solver(joltage, button):
            opt = Optimize()

            press_counts = [Int(f"c_{i}") for i in range(len(button))]

            for count in press_counts:
                opt.add(count >= 0)

            # Assign button to joltage index
            for pos, jol in enumerate(joltage):
                affects = [
                    press_counts[i]
                    for i, btn in enumerate(button) if pos in btn]

                opt.add(Sum(affects) == jol)

            # Minimize total presses
            opt.minimize(Sum(press_counts))

            if opt.check() != sat:
                raise ValueError("No solution found.")

            model = opt.model()
            return sum(model[c].as_long() for c in press_counts)

        return sum(
            solver(joltage, button)
            for joltage, button in zip(joltages, buttons))


def test() -> None:
    """Run with example puzzle input."""
    inp = Solution.read_input("example.txt")

    assert Solution.part_1(inp) == 7
    assert Solution.part_2(inp) == 33

    print("Both tests passed!")


def run() -> None:
    """Run with actual puzzle input."""
    inp = Solution.read_input("input.txt")

    print(f"Solution to part 1: {Solution.part_1(inp)}")
    print(f"Solution to part 2: {Solution.part_2(inp)}")


if __name__ == "__main__":
    try:
        run_mode = sys.argv[1]
    except IndexError:
        run()
        sys.exit()

    if run_mode in ["-r", "--run"]:
        run()
    elif run_mode in ["-t", "--test"]:
        test()
