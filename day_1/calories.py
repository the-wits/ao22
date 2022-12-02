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


def top_calories(input):
    elves = parse_file(input)    
    return max(elves)


def top_three_calories(input):
    elves = parse_file(input)
    elves.sort(reverse=True)
    return elves[0] + elves[1] + elves[2]


if __name__ == "__main__":
    print("\n--- Day 1: Calorie Counting ---")
    max_cal = top_calories("input.txt")
    print(f"\n[+] Max calories: {max_cal}")

    top_3 = top_three_calories("input.txt")
    print(f"[+] Top 3 calories (sum): {top_3}\n")
