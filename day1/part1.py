from day1 import *

def main():
    rotations = parse_rotations("input.txt")
    dial_position = STARTING_DIAL_POSITION
    password_num = 0
    for distance in rotations:
        dial_position = (dial_position + distance) % STEPS
        if dial_position == 0:
            password_num += 1
    print("PASSWORD:", password_num)

if __name__ == "__main__":
    main()