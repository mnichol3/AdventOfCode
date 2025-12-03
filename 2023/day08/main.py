"""
Advent of Code 2023
Day 8 - Haunted Wasteland
"""
import re
from pathlib import Path
from typing import Dict, List, Tuple


def read_input() -> Tuple[List[str], Dict[str, List[str]]]:
    """Read and clean/organize the input."""
    input = Path(__file__).with_name('input.txt').read_text().splitlines()

    instructions = list(input[0])

    nodes = {}
    for x in input[1:]:
        if x == '':
            continue

        key, val = x.split(' = ')
        val = re.findall(r'\w+', val)
        nodes[key] = val

    return instructions, nodes


def solve_1(instructions: list[str], nodes: Dict[str, list[str]]) -> None:
    """Solution for Part 1."""
    curr_node = 'AAA'
    idx = 0
    num_instrs = len(instructions)

    while curr_node != 'ZZZ':
        curr_step = instructions[idx % num_instrs]
        step_idx = 0 if curr_step == 'L' else 1

        curr_node = nodes[curr_node][step_idx]

        idx += 1

    print(idx)


def solve_2() -> None:
    """Solution for Part 2."""
    raise NotImplementedError


def test_1() -> None:
    instr = list('LLR')
    nodes = {
        'AAA': ['BBB', 'BBB'],
        'BBB': ['AAA', 'ZZZ'],
        'ZZZ': ['ZZZ', 'ZZZ'],
    }

    solve(instr, nodes)


def test_2() -> None:
    raise NotImplementedError


def main() -> None:
    instr, nodes = read_input()
    solve_1(instr, nodes)


if __name__ == '__main__':
    main()
    #test()