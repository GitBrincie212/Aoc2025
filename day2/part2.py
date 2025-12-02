from day2 import parse_ranges, count_digits


def main():
    [num_ranges, max_num] = parse_ranges("./input.txt")
    max_num_digits = count_digits(max_num)
    invalid_sums = 0
    repeaters = set()
    for n in range(2, max_num_digits):
        x = 1
        while True:
            repeated = int(str(x) * n)
            if repeated >= max_num or count_digits(repeated) > max_num_digits:
                break
            repeaters.add(repeated)
            x += 1

    for repeat in repeaters:
        for num_range in num_ranges:
            if num_range[0] <= repeat <= num_range[1]:
                invalid_sums += repeat

    print(invalid_sums)


if __name__ == "__main__":
    main()