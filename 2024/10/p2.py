"""Advent of Code 2024 - Day 10 Part 2"""
from __future__ import annotations

from p1 import parse_input, Graph


graph = Graph(parse_input())

sum = 0
for start_node in graph.roots:
    sum += len(graph.part2(start_node, [], []))

print(f'Answer: {sum}')
