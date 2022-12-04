#!/usr/bin/python3


def parse_file(input):
    elves = []

    with open(input, "r") as input:
        kcal = input.read().splitlines()
        elf = 0
        for value in kcal:
            if value == '':
                elves.append(elf)
                elf = 0
            else:
                elf += int(value)
    
    return elves


def top_calories(elves):
    return max(elves)


def top_three_calories(elves):
    elves.sort(reverse=True)
    return elves[0] + elves[1] + elves[2]


if __name__ == "__main__":
    print("\n--- Day 1: Calorie Counting ---")
    elves = parse_file("input.txt")

    max_cal = top_calories(elves)
    print(f"\n[+] Max calories: {max_cal}")

    top_3 = top_three_calories(elves)
    print(f"[+] Top 3 calories (sum): {top_3}")
