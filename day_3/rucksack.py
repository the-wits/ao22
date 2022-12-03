#!/usr/bin/python3

def get_bags(input):
    bags = []
    with open(input, "r") as input_file:
        lines = input_file.read().splitlines()
        for line in lines:
            bags.append([line[:len(line)//2], line[len(line)//2:]])

    return bags


def get_score(item):
    if item.islower():
        return ord(item) - 97 + 1
    else:
        return ord(item) - 65 + 27


def get_priorities(input):
    priorities = 0
    bags = get_bags(input)

    for bag in bags:
        item = list(set(bag[0]) & set(bag[1]))[0]
        priorities += get_score(item)

    return priorities


def get_groups(input):
    with open(input, "r") as input_file:
        lines = input_file.read().splitlines()
        i = 0
        group = []
        groups = []
        for line in lines:
            if i > 2:
                groups.append(group)
                group = [line]
                i = 1
            else:
                group.append(line)
                i += 1
        groups.append(group)

    return groups


def get_badge_priorities(input):
    priorities = 0
    groups = get_groups(input)

    for group in groups:
        item = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
        priorities += get_score(item)

    return priorities


if __name__ == "__main__":
    print("\n--- Day 3: Rucksack Reorganization ---")
    priorities = get_priorities("input.txt")
    print(f"\n[+] Priorities (sum): {priorities}")
    badge_prior = get_badge_priorities("input.txt")
    print(f"[+] Badge priorities (sum): {badge_prior}")
