#!/usr/bin/python3


def parse_file(input):
    output = []
    with open(input, "r") as input_file:
        lines = input_file.read().splitlines()
        for line in lines:
            # Example of line: 2-4,6-8
            line = line.split(",")
            first = line[0].split('-')
            second = line[1].split('-')
            output.append([
                [int(first[0]), int(first[1])],
                [int(second[0]), int(second[1])]
            ])

    return output


def get_contained(pairs):
    contained = 0

    for pair in pairs:
        if (pair[0][0] <= pair[1][0] and pair[1][1] <= pair[0][1]) \
                or (pair[1][0] <= pair[0][0] and pair[0][1] <= pair[1][1]):
            contained += 1

    return contained


def get_overlapped(pairs):
    overlapped = 0

    for pair in pairs:
        if pair[0][0] <= pair[1][0] <= pair[0][1] \
                or pair[0][0] <= pair[1][1] <= pair[0][1] \
                or pair[1][0] <= pair[0][0] <= pair[1][1] \
                or pair[1][0] <= pair[0][1] <= pair[1][1]:
            overlapped += 1

    return overlapped


if __name__ == "__main__":
    print("\n--- Day 4: Camp Cleanup ---")
    pairs = parse_file("input.txt")

    value = get_contained(pairs)
    print(f"\n[+] Pairs fully contained: {value}")

    value = get_overlapped(pairs)
    print(f"[+] Overlapped pairs: {value}")
