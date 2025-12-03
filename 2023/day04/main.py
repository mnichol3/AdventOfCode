"""
Advent of Code
Day 4 - Scratchcards
"""
import re
from pathlib import Path


SAMPLE_INP = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
]


class Card:

    def __init__(
        self,
        number: int,
        winning_numbers: list[int],
        test_numbers: list[int],
        copies: int = 1
    ) -> None:
        self.number = number
        self.test_numbers = test_numbers
        self.winning_numbers = winning_numbers
        self.copies = copies
        self.matches = [x for x in self.test_numbers if x in self.winning_numbers]

    @property
    def num_matches(self) -> int:
        return len(self.matches)


def clean_line(line: str) -> tuple[list[str]]:
    """Split a card into winning numbers and 'your' numbers."""
    nums = line.split(':')[1]
    winning, test = [re.findall(r'\d+', x) for x in nums.split('|')]

    return winning, test


def str_to_list(int_str: str, delim: str = ' ') -> list[int]:
    """Convert a list of strings to integers."""
    return [int(x) for x in int_str.split(delim) if x != '']


def solve_1(text: list[str]) -> int:
    """
    Solution to Part 1.
    """
    ttl_points = 0

    for line in text:
        winning_nums, my_nums, = clean_line(line)

        my_nums = str_to_list(my_nums)
        winning_nums = str_to_list(winning_nums)

        matches = [x for x in my_nums if x in winning_nums]

        card_points = 0 if not matches else 2 ** (len(matches) - 1)

        ttl_points += card_points

    return ttl_points


def solve_2(text: list[str]) -> int:
    """
    Solution to Part 2.
    """
    cards = {}

    for idx, line in enumerate(text):
        card_idx = idx + 1
        winning_nums, my_nums = clean_line(line)
        cards[card_idx] = Card(card_idx, winning_nums, my_nums)

    for key, val in cards.items():
        matches = val.matches

        for i in range(len(matches)):
            cards[key + i + 1].copies += val.copies

    return sum([x.copies for x in cards.values()])


if __name__ == '__main__':
    cards = Path(__file__).with_name('input.txt').read_text().split('\n')

    #soln = solve_1(cards)
    soln = solve_2(cards)

    print(soln)
