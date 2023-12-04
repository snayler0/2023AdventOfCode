if __name__ == "__main__":

    with open("input", "r") as file:
        input_lines = file.read().splitlines()

    running_total = 0

    for line in input_lines:
        first_digit = next(char for char in line if char.isdigit())
        last_digit = next(char for char in reversed(line) if char.isdigit())

        line_digit = int(f"{first_digit}{last_digit}")

        running_total += line_digit

    print(f"final result was {running_total}")
