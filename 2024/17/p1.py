"""Advent of Code 2024 - Day 17 Part 1"""
from __future__ import annotations
import re
from dataclasses import dataclass
from math import trunc
from pathlib import Path


def parse_input(f_path: str = 'input.txt') -> tuple[list[int], list[int]]:
    """Read and return input from text file.

    Parameters
    ----------
    f_path: str, optional
        Input file path. Default is 'input.txt'.

    Returns
    -------
    list of int
        Processor register initial values.
    list of int
        Processor instructions.
    """
    patt = re.compile(r'Register \w\: (\d+)')
    inp = Path(f_path).read_text().split('\n\n')

    reg_vals = list(map(int, patt.findall(inp[0])))
    pgm = list(map(int, inp[1].split(' ')[1].strip().split(',')))

    return reg_vals, pgm


@dataclass
class Registers:
    """Simple container for registers."""
    A: int
    B: int
    C: int


class Processor:
    """Simple processor class."""

    def __init__(self, reg_vals: list[int]) -> None:
        """Constructor.

        Parameters
        ----------
        reg_vals: list of int
            Initial values for registers A, B, and C.

        Returns
        -------
        None.
        """
        self.registers = Registers(*reg_vals)
        self.ptr = 0

    def _get_combo_operand(self, oper: int) -> int:
        """Get the combo operand for the given literal operand."""
        if oper in [0, 1, 2, 3, 7]:
            return oper

        if oper == 4:
            return self.registers.A
        elif oper == 5:
            return self.registers.B
        elif oper == 6:
            return self.registers.C

    def _instr0(self, oper: int) -> None:
        """instruction 0 - adv"""
        self.registers.A = trunc(self.registers.A
                                 / (2**self._get_combo_operand(oper)))

    def _instr1(self, oper: int) -> None:
        """instruction 1 - bxl"""
        self.registers.B = self.registers.B ^ oper

    def _instr2(self, oper: int) -> None:
        """instruction 2 - bst"""
        self.registers.B = self._get_combo_operand(oper) % 8

    def _instr3(self, oper: int) -> None:
        """instruction 3 - jnz"""
        if self.registers.A != 0:
            self.ptr = oper - 2

    def _instr4(self, oper: int) -> None:
        """instruction 4 - bxc"""
        _ = oper
        self.registers.B = self.registers.B ^ self.registers.C

    def _instr5(self, oper: int) -> int | str:
        """instruction 5 - out"""
        return self._get_combo_operand(oper) % 8

    def _instr6(self, oper: int) -> None:
        """instruction 6 - bdv"""
        self.registers.B = trunc(self.registers.A
                                 / (2**self._get_combo_operand(oper)))

    def _instr7(self, oper: int) -> None:
        """instruction 7 - cdv"""
        self.registers.C = trunc(self.registers.A
                                 / (2**self._get_combo_operand(oper)))

    def run_program(self, pgm: str) -> str:
        """Run a program.

        Parameters
        ----------
        pgm: list of int
            Program to run.

        Returns
        -------
        str
            Comma-separated output.
        """
        self.ptr = 0
        output = []
        while self.ptr < len(pgm) - 1:
            instr = pgm[self.ptr]
            operand = pgm[self.ptr+1]
            rtn = getattr(self, f'_instr{instr}')(operand)

            if rtn is not None:
                output.append(str(rtn))

            self.ptr += 2

        return ','.join(output)

    def __repr__(self) -> str:
        """Return a string representation of the class."""
        return (f'<{self.__class__.__name__} A={self.registers.A}, '
                f'B={self.registers.B}, C={self.registers.C}>')


if __name__ == '__main__':
    reg_vals, program = parse_input()

    proc = Processor(reg_vals)
    rtn = proc.run_program(program)

    print(f'Part 1 answer: {rtn}')
