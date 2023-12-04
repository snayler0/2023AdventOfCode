import re
import math

MAX_COLOUR = {"RED": 12, "GREEN": 13, "BLUE": 14}


def find_largest_num_of_cubes_per_colour(game):
    minimum_required_colour = {"RED": 0, "GREEN": 0, "BLUE": 0}

    for round in game:
        round = round.strip()

        per_colour = count_cubes_per_colour_in_round(round)

        for colour in per_colour.keys():
            if per_colour[colour] > minimum_required_colour[colour]:
                minimum_required_colour[colour] = per_colour[colour]

    return minimum_required_colour


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
    match = re.search(r"Game (\d+):", line)
    game_number = int(match.group(1))

    # Cleanup the input
    line = line.strip(" ").split(":")[1]
    rounds = line.strip(" ").split(";")

    minimum_required_colour = find_largest_num_of_cubes_per_colour(rounds)
    game_power = math.prod(minimum_required_colour.values())
    game_possible = True

    for key, value in minimum_required_colour.items():
        if minimum_required_colour[key] > MAX_COLOUR[key]:
            game_possible = False
            print(f"Game {game_number} is impossible")
            print(
                f"Because {minimum_required_colour[key]} {key} cubes is more than the max {MAX_COLOUR[key]} {key} cubes"
            )
    return game_number, game_power, game_possible


def read_input():
    with open("input", "r") as file:
        input_lines = file.read().splitlines()

    return input_lines


if __name__ == "__main__":
    input_lines = read_input()

    powers = []
    possible_games = []

    for line in input_lines:
        game_number, game_power, possible = are_results_possible(line)

        print(f"Game: {game_number}")

        powers.append(game_power)

        if possible:
            possible_games.append(game_number)

    print(f"Sum of possible game ID's: {sum(possible_games)}")
    print(f"The sum of the power of the minimum set of cubes for all games to be possible was: {sum(powers)}")
