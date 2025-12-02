import math

def count_digits(x: int) -> int:
    return math.floor(math.log10(x)) + 1

def parse_ranges(input_path: str) -> [tuple[int, int], int]:
    with open(input_path, "r") as f:
        data = f.read()
        splitted = data.strip("\n").strip(" ").split(",")
        num_ranges = []
        max_num = None
        for num_range in splitted:
            split = num_range.split("-")
            [num1, num2] = [int(split[0]), int(split[1])]
            if (not max_num) or num2 > max_num:
                max_num = num2
            num_ranges.append((num1, num2))
        return [num_ranges, max_num]