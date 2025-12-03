"""
Welcome to the dumpster fire.
"""
from typing import Dict
from pathlib import Path


class SeedMap:

    def __init__(self, map_list: list[float, float, float]) -> None:
        self.dest_range = map_list[0]
        self.src_range = map_list[1]
        self.range_length = map_list[2]

        self.dest_list = []
        self.src_list = []

    def expand(self) -> None:
        for attr in ['dest_range', 'src_range']:
            val = getattr(self, attr)
            rng = range(getattr, getattr + self.range_length, 1)
            setattr(attr.replace('range', 'list'), rng)

    def __repr__(self) -> str:
        return f'<SeedMap {self.dest_range}, {self.src_range}, {self.range_length}>'


def read_input(path: Path) -> None:

    def _clean_line(line):
        line_str = line.strip()
        ints = [int(x) for x in line_str.split(' ') if x != '']

        return ints

    data = {}
    curr_name = ''

    with open(path, 'r') as f_in:
        for line in f_in:
            if ':' in line:
                parts = line.split(':')
                curr_name = parts[0]

                if parts[1] == '\n':
                    data[curr_name] = {}
                else:
                    data[curr_name] = _clean_line(parts[1])
            elif line[0] != '\n':
                my_map = SeedMap(_clean_line(line))
                my_dict = {my_map.dest_range: my_map}

                if curr_name in data.keys():
                    data[curr_name].update(my_dict)
                else:
                    data[curr_name] = my_dict

    return data


def fill_zeros(data_dict: Dict[float, SeedMap]) -> Dict:
    pass


if __name__ == '__main__':
    input_file = Path('input.txt')

    input = read_input(input_file)
    print(input)

    for key, val in input.items():
        print(key, len(val))
