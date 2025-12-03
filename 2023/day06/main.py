"""
Advent of Code 2023
Day 6 - "Wait for It"
"""


def solve(race_time: float, record_dist: float) -> float:
    num_records = 0

    for hold_time in range(race_time + 1):
        dist = hold_time * (race_time - hold_time)

        if dist > record_dist:
            num_records += 1

    return num_records


if __name__ == '__main__':
    # Race time and distances go here
    race_data = [
        [],
    ]

    prod = 1
    for race in race_data:
        prod *= solve(race[0], race[1])

    print(prod)
