"""Advent of Code 2024 - Day 13 Part 1 & 2"""
from __future__ import annotations
import re
from dataclasses import dataclass
from pathlib import Path


class Button:

    def __init__(self, name, x: int, y: int, cost: int):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.cost = int(cost)

    def __repr__(self) -> str:
        sub_str = f'{self.name} X+{self.x}, Y+{self.y}'
        return f'<{self.__class__.__qualname__} {sub_str}>'


@dataclass
class ButtonContainer:
    A: Button
    B: Button


class ClawMachine:

    def __init__(
        self,
        button_a: tuple[int, int],
        button_b: tuple[int, int],
        prize: tuple[int, int],
    ):
        self.buttons = ButtonContainer(
            Button('A', *button_a, 3),
            Button('B', *button_b, 1),
        )
        self.prize = prize

    def solve(self, part2: bool = False) -> int:

        def _is_int(x: int) -> bool:
            return round(x, 2).is_integer()

        prize_x = self.prize[0]
        prize_y = self.prize[1]

        if part2:
            prize_x += 10e12
            prize_y += 10e12

        c = prize_x / self.buttons.A.x
        d = self.buttons.B.x / self.buttons.A.x
        b = ((prize_y - (self.buttons.A.y*c))
             / (self.buttons.B.y - (self.buttons.A.y*d)))

        a = c - d * b

        if _is_int(a) and _is_int(b) and a > 0 and b > 0:
            return (a*self.buttons.A.cost) + (b*self.buttons.B.cost)

        return 0

    @classmethod
    def from_file(cls, f_path: str = 'input.txt') -> list[ClawMachine]:
        machines = []
        for block in Path(f_path).read_text().split('\n\n'):
            inp = re.findall(r'X[\+|\=](\d{1,6}), Y[\+|\=](\d{1,6})', block)
            machines.append(
                cls(
                    tuple(map(int, inp[0])),
                    tuple(map(int, inp[1])),
                    tuple(map(int, inp[2])),
                ))

        return machines

    def __repr__(self) -> str:
        prize = f'<Prize X={self.prize[0]}, Y={self.prize[1]}'
        sub_str = f'{self.buttons.A}, {self.buttons.B}, {prize}>'
        return f'<{self.__class__.__qualname__} {sub_str}>'


if __name__ == '__main__':
    sum = 0
    for m in ClawMachine.from_file():
        sum += m.solve(True)

    print(f'Answer: {int(sum)}')
