#!/usr/bin/python3

def parse_file(name):
    with open(name, "r") as input_file:
        return input_file.readline()


def get_marker(stream, length):
    window = ''
    for i in range(0, len(stream)):
        # mjqjpqmgbljsphdztnvjfqwrcgsmlb
        if not stream[i] in window:
            window += stream[i]
        else:
            window = window.split(stream[i], 1)[1]
            window += stream[i]

        if len(window) == length:
            return i + 1


if __name__ == "__main__":
    stream = parse_file("input.txt")
    print("\n--- Day 6: Tuning Trouble ---")

    value = get_marker(stream, 4)
    print(f"\n[+] Packet starts after: {value} characters")

    value = get_marker(stream, 14)
    print(f"[+] Message starts after: {value} characters")
