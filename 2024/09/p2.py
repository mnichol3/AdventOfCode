"""Advent of Code 2024 - Day 9 Part 2"""
from p1 import parse_input


def part2(disk: list[int]) -> int:
    """Solution to Part 2.

    Parameters
    ----------
    list of list of int

    Returns
    -------
    int
    """
    mem_map = []
    for i, num in enumerate(disk):
        idx = None if i % 2 else i // 2
        size = int(num)
        if size > 0:
            mem_map.append([idx, size])

    i = 0
    while i < len(mem_map):
        i += 1
        idx, size = mem_map[-i]
        if idx is None:
            continue

        for j in range(len(mem_map) - i):
            if mem_map[j][0] is None and mem_map[j][1] >= size:
                if mem_map[j][1] == size:
                    mem_map[j][0] = idx
                else:
                    mem_map[j][1] -= size
                    mem_map.insert(j, mem_map[-i].copy())
                mem_map[-i][0] = None
                break

    total = idx = 0
    for id, size in mem_map:
        if id is not None:
            total += id * size * (idx + ((size - 1) / 2))
        idx += size

    return int(total)


if __name__ == '__main__':
    inp = parse_input()
    print(f'Day 09 Part 2 answer: {part2(inp)}')