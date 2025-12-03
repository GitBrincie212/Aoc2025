from typing import Generator

from day3 import parse_batteries

# I'm not proud of this code whatsoever, but eh whatever, it ain't production code
def activate_twice(bank: Generator[int, None, None]) -> int:
    bank = list(bank)
    idx, max1 = max(enumerate(bank), key=lambda x: x[1])
    return (max1 * 10) + max(bank[idx + 1:]) if idx < len(bank) - 1 else (max(bank[:idx]) * 10) + max1

def main():
    banks = parse_batteries("./example_input.txt")
    print(sum(activate_twice(bank) for bank in banks))

if __name__ == "__main__":
    main()