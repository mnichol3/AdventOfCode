import re
from pathlib import Path


SAMPLE_INP = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]


def word2num(word: str) -> str:
    digits = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    digits.update({str(i): str(i) for i in range(10)})

    numbers = re.compile('|'.join(digits))

    return ''.join(digits[w] for w in numbers.findall(word))


def solve_1(text: list[str]) -> None:
    sum = 0

    for line in text:
        integers = re.findall(r'\d', line)
        strs = [str(x) for x in integers]

        if len(strs) < 2:
            strs.append(strs[0])

        val = int(f'{strs[0]}{strs[-1]}')

        sum += val

    print(sum)


def solve_2(text: list[str]) -> None:
    digits = {
        'zero': 'z0ro',
        'one': 'o1e',
        'two': 't2o',
        'three': 'th3ee',
        'four': 'f4ur',
        'five': 'f5ve',
        'six': 's6x',
        'seven': 'se7en',
        'eight': 'ei8ht',
        'nine': 'n9ne'
    }
    sum = 0

    for line in text:
        for key, val in digits.items():
            line = line.replace(key, val)

        curr_line = word2num(line)

        num = f'{curr_line[0]}{curr_line[-1]}'
        print(curr_line, line, num)
        sum += int(num)

    print(sum)


if __name__ == '__main__':
    raw_inp = Path(__file__).with_name('input.txt').read_text().splitlines()

    text = [x.strip() for x in raw_inp]

    #solve_1(text)
    solve_2(text)
