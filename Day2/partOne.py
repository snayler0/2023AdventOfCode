import re

MAX_COLOUR = {"RED": 12, "GREEN": 13, "BLUE": 14}


def count_cubes_per_colour_in_round(round):
    print(f"Round: {round}")

    # Split the input string into individual color and number pairs
    colour_number_pairs = [pair.strip() for pair in round.split(",")]

    colour_dict = {}
    for pair in colour_number_pairs:
        parts = pair.split()
        if len(parts) == 2:
            number, colour = int(parts[0]), parts[1]
            colour_dict[colour.upper()] = number

    return colour_dict


def are_results_possible(line):

    largest_colour = {"RED": 0, "GREEN": 0, "BLUE": 0}

    match = re.search(r"Game (\d+):", line)
    game_number = int(match.group(1))

    # Cleanup the input
    line = line.strip(" ").split(":")[1]
    rounds = line.strip(" ").split(";")

    for round in rounds:
        round = round.strip()
        per_colour = count_cubes_per_colour_in_round(round)

        for colour in per_colour.keys():
            if per_colour[colour] > largest_colour[colour]:
                largest_colour[colour] = per_colour[colour]

    game_possible = True

    for key, value in largest_colour.items():
        if largest_colour[key] > MAX_COLOUR[key]:
            game_possible = False
            print(f"Game {game_number} is impossible")
            print(
                f"Because {largest_colour[key]} {key} cubes is more than the max {MAX_COLOUR[key]} {key} cubes"
            )
    return game_number, game_possible


def read_input():
    with open("input", "r") as file:
        input_lines = file.read().splitlines()

    return input_lines


if __name__ == "__main__":
    input_lines = read_input()

    possible_sum = 0

    for line in input_lines:
        game_number, possible = are_results_possible(line)

        print(f"Game: {game_number}")

        if possible:
            possible_sum += game_number

    print(f"Sum of possible game ID's: {possible_sum}")
