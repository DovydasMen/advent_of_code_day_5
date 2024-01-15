from typing import List, Generator
from pathlib import Path
from pprint import pprint


def get_seeds(lines: List[str]) -> Generator:
    """(int(value) for value in full_almanac[0].split() if value.isdigit())
    Same as below in my case readability is better with function
    """

    line_values = lines[0].split()
    for value in line_values:
        if value.isdigit():
            yield int(value)


def get_alignment_map(almanac: List[str]) -> Generator:
    ally = []
    counter = -1
    for value in almanac[1:]:
        if value == "":
            continue
        elif value.endswith(":"):
            ally.append([])
            counter += 1
        else:
            ally[counter].append([int(val) for val in value.split()])

    for aligment in ally:
        yield aligment


def get_locations(seeds: Generator, alignment_map: Generator) -> List[int]:
    locations = []
    for seed in seeds:
        location = seed
        for ally_map in alignment_map:
            for value in ally_map:
                destination, source, symbols_range = value
                if location in range(int(source), int(source) + int(symbols_range)):
                    diffrence = location - int(source)
                    location = int(destination) + int(diffrence)
                    break
        locations.append(location)
    return locations


if __name__ == "__main__":
    full_almanac = Path("input.txt").read_text().splitlines()
    seeds = get_seeds(full_almanac)
    alignment_map = get_alignment_map(full_almanac)
    print(min(get_locations(seeds=seeds, alignment_map=alignment_map)))
