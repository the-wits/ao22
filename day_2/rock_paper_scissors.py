#!/usr/bin/python3


def parse_file(input):
    rounds = []

    with open(input, "r") as input:
        lines = input.read().splitlines()
        for line in lines:
            rounds.append((line).split(" "))
    
    return rounds


def get_first_score(opponent, player):
    rock, paper, scissors = 1, 2, 3
    lost, draw, win = 0, 3, 6
    
    # Rock vs Rock
    if opponent == "A" and player == "X":
        return rock + draw
    
    # Rock vs Paper
    if opponent == "A" and player == "Y":
        return paper + win
    
    # Rock vs Scissors
    if opponent == "A" and player == "Z":
        return scissors + lost

    # Paper vs Rock
    if opponent == "B" and player == "X":
        return rock + lost
    
    # Paper vs Paper
    if opponent == "B" and player == "Y":
        return paper + draw
    
    # Paper vs Scissors
    if opponent == "B" and player == "Z":
        return scissors + win

    # Scissors vs Rock
    if opponent == "C" and player == "X":
        return rock + win
    
    # Scissors vs Paper
    if opponent == "C" and player == "Y":
        return paper + lost
    
    # Scissors vs Scissors
    if opponent == "C" and player == "Z":
        return scissors + draw


def get_second_score(opponent, player):
    rock, paper, scissors = 1, 2, 3
    lost, draw, win = 0, 3, 6
    
    # Rock vs Scissors
    if opponent == "A" and player == "X":
        return scissors + lost
    
    # Rock vs Rock
    if opponent == "A" and player == "Y":
        return rock + draw
    
    # Rock vs Paper
    if opponent == "A" and player == "Z":
        return paper + win

    # Paper vs Rock
    if opponent == "B" and player == "X":
        return rock + lost
    
    # Paper vs Paper
    if opponent == "B" and player == "Y":
        return paper + draw
    
    # Paper vs Scissors
    if opponent == "B" and player == "Z":
        return scissors + win

    # Scissors vs Paper
    if opponent == "C" and player == "X":
        return paper + lost
    
    # Scissors vs Scissors
    if opponent == "C" and player == "Y":
        return scissors + draw
    
    # Scissors vs Rock
    if opponent == "C" and player == "Z":
        return rock + win


def get_score(rounds, score_type):
    score = 0

    for round in rounds:
        if score_type == 1:
            score += get_first_score(round[0], round[1])
        elif score_type == 2:
            score += get_second_score(round[0], round[1])

    return score


if __name__ == "__main__":
    print("\n--- Day 2: Rock Paper Scissors ---")
    rounds = parse_file("input.txt")
    first_score = get_score(rounds, 1)
    print(f"\n[+] 1st Score: {first_score}")
    second_score = get_score(rounds, 2)
    print(f"[+] 2nd Score: {second_score}")
