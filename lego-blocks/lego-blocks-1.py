import itertools
import math


def break_combinations_for_one_line(width):
    min_blocks = int(math.floor(width / 4.0))
    max_blocks = width
    for num_blocks in range(min_blocks, max_blocks + 1):
        for combination in itertools.product((1, 2, 3, 4), repeat=num_blocks):
            if sum(combination) == width:
                yield tuple(itertools.accumulate(combination))[:-1]


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
