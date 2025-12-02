
from day1 import *

def main():
    rotations = parse_rotations("input.txt")
    dial_position = STARTING_DIAL_POSITION
    password_num = 0
    for distance in rotations:
        # This is an adapted solution from https://github.com/maneatingape/advent-of-code-rust/blob/main/src/year2025/day01.rs
        if distance > 0:
            password_num += (dial_position + distance) // 100
        else:
            reversed_ = (STEPS - dial_position) % STEPS
            password_num += (reversed_ - distance) // 100

        dial_position = (dial_position + distance) % STEPS

    print("PASSWORD: ", password_num)

if __name__ == "__main__":
    main()