from typing import Generator


def parse_batteries(input_path: str) -> list[Generator[int, None, None]]:
    with open(input_path, "r") as f:
        data = f.read()
        splitted = data.split("\n")
        return [
            map(int, bank)
            for bank in splitted
        ]