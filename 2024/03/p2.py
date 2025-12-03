"""Advent of Code 2024 - Day 3 Part 2"""
import re

from p1 import parse_input


def answer(instructions: list[str]) -> int:
    """Compute the answer for Part 2.

    Parameters
    ----------
    instructions: list of str
        Instructions to parse.

    Returns
    -------
    int
        Sum of valid multiplication instructions.
    """
    mul_on = True
    total = 0
    patt = re.compile(r"(do)\(\)|(don't)\(\)|mul\((\d{1,3})\,(\d{1,3})\)")

    for instr in instructions:
        valid = patt.findall(instr)

        for x in valid:
            if x[0] == 'do':
                mul_on = True
            elif x[1] == "don't":
                mul_on = False
            else:
                if mul_on:
                    total += int(x[2]) * int(x[3])

    return total


if __name__ == '__main__':
    print(f'Day 03 Part 2 answer: {answer(parse_input())}')
