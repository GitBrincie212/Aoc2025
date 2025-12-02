from typing import Final

STEPS: Final[int] = 100
STARTING_DIAL_POSITION: Final[int] = 50

def parse_rotations(input_path: str) -> list[int]:
    with open(input_path, "r") as f:
        data = f.read()
        splitted = data.split("\n")
        rotations = []
        for line in splitted:
            direction = -1 if line[0] == "L" else 1
            distance = int(line[1:])
            rotations.append(direction * distance)
        return rotations