"""Advent of Code 2024 - Day 17 Part 2"""
import p1


def run_a(a: int) -> list[int]:
    """Compute the value of the A register by running a stripped-down version
    of the program.
    """
    b = 0
    c = 0
    output = []

    while a:
        b = a % 8
        b = b ^ 2
        c = a // 2**b
        a = a // 2**3
        b = b ^ c
        b =  b ^ 7
        output.append(b % 8)

    return output


def reverse_prog(program: list[str]) -> int:
    valid_vals = {0}

    for instr in reversed(program):
        curr_vals = set()

        for v in valid_vals:
            shifted = v * 8

            for x in range(shifted, shifted+8):
                output = run_a(x)
                if output and output[0] == instr:
                    curr_vals.add(x)

        valid_vals = curr_vals

    return min(valid_vals)


if __name__ == '__main__':
    reg_vals, program = p1.parse_input()

    ans = reverse_prog(program)

    # Validate our answer
    truth = ','.join([str(x) for x in program])
    test = p1.Processor([ans] + reg_vals[1:]).run_program(program)

    assert test == truth, f'Validation failed: {test} != {truth}'

    print(f'Part 2 answer: {ans}')
