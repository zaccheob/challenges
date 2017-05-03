import itertools
import math

MAX_BLOCK_LEN = 4


def _combinations_for_maxblock_line(w):
    if w == 0:
        yield ()
    else:
        yield((w,))
        for i in range(1,w):
            for c in itertools.product(combinations_for_maxblock_line(i), combinations_for_maxblock_line(w-i)):
                yield tuple(itertools.chain(*c))


def combinations_for_maxblock_line(w):
    return tuple(sorted(set(_combinations_for_maxblock_line(w))))


def combinations_for_n_maxblocks_line(n):
    for c in itertools.product(combinations_for_maxblock_line(MAX_BLOCK_LEN), repeat=n):
        yield tuple(itertools.chain(*c))


def _combinations_for_line(w):
    combinations_for_remainder = tuple(combinations_for_maxblock_line(w % MAX_BLOCK_LEN))
    combinations_for_n_maxblocks = tuple(combinations_for_n_maxblocks_line(int(w / MAX_BLOCK_LEN)))
    for l in (
            (combinations_for_n_maxblocks, combinations_for_remainder),
            (combinations_for_remainder, combinations_for_n_maxblocks)):
        for c in itertools.product(*l):
            yield c[0] + c[1]


def combinations_for_line(w):
    return tuple(sorted(set(_combinations_for_line(w))))


def break_combinations_for_one_line(w):
    for c in combinations_for_line(w):
        yield tuple(itertools.accumulate(c))[:-1]


def check_wall_breaks(wall):
    return not any([all([first_line_break in l for l in wall[1:]]) for first_line_break in wall[0]])


def number_of_ways(wall_height, wall_width):
    count = 0
    for wall_breaks in itertools.product(break_combinations_for_one_line(wall_width), repeat=wall_height):
        if check_wall_breaks(wall_breaks):
            count += 1
    return count


def main():
    number_of_tests = int(input())
    for _ in range(0, number_of_tests):
        wall_height, wall_width = [int(x) for x in input().split()]
        print(number_of_ways(wall_height, wall_width))


if __name__ == '__main__':
    main()
