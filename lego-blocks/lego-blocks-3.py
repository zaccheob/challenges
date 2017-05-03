import math


def multiple_consecutive_numbers_having_sum(max_n, sum):
    if max_n == 1:
        yield (sum,)
    else:
        for i in range(math.floor(sum/max_n), -1, -1):
            for r in multiple_consecutive_numbers_having_sum(max_n - 1, sum - i * max_n):
                yield (i,) + r


def product(l):
    out = 1
    for x in l:
        out *= x
    return out


def number_of_ways_to_build_one_row(max_n, wall_width):
    return int(sum(map(lambda x: math.factorial(sum(x))/product(map(lambda y: math.factorial(y), x)),
                   multiple_consecutive_numbers_having_sum(max_n, wall_width))))


def number_of_ways(wall_height, wall_width):
    return 1


def main():
    number_of_tests = int(input())
    for _ in range(0, number_of_tests):
        wall_height, wall_width = [int(x) for x in input().split()]
        print(number_of_ways(wall_height, wall_width))


if __name__ == '__main__':
    print(number_of_ways_to_build_one_row(4, 10))
    #main()
