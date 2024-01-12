from typing import List, Tuple


def read_lines_from_file(file_path) -> List[str]:
    """Read lines from a file, trims whitespace and ignores empty lines."""
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]


def get_seeds(lines: list) -> list:
    return list(map(int, lines[0].strip("seeds: ").split()))


def get_almanac_without_seeds(full_almanac: List[str]) -> Tuple[List[int], List[str]]:
    seeds = get_seeds(full_almanac)
    del full_almanac[0]
    return seeds, full_almanac


def get_mapping_map(map: List[str]) -> List[List[int]]:
    mapping_map = [[]]
    mapping_place = -1

    for value in map:
        if value.endswith(":"):
            mapping_place += 1
            mapping_map.append([])
            continue
        else:
            mapping_map[mapping_place].append([int(number) for number in value.split()])

    return mapping_map


def get_locations(seeds: List[int], mapping_map: List[List[int]]) -> List[int]:
    locations = []
    for seed in seeds:
        location = seed
        for mapping in mapping_map:
            for details in mapping:
                if location in range(details[1], details[1] + details[2]):
                    destination, source, _ = details
                    diffrence = location - source
                    location = destination + diffrence
                    break
        locations.append(location)

    return locations


if __name__ == "__main__":
    full_almanac = read_lines_from_file("input.txt")
    seeds, almanac_without_seeds = get_almanac_without_seeds(full_almanac)
    mapping_map = get_mapping_map(almanac_without_seeds)
    print(min(get_locations(mapping_map=mapping_map, seeds=seeds)))
