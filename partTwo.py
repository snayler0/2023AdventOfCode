NUMBERS = {
    "ONE": "O1NE",
    "TWO": "T2WO",
    "THREE": "T3HREE",
    "FOUR": "F4OUR",
    "FIVE": "F5IVE",
    "SIX": "S6IX",
    "SEVEN": "S7EVEN",
    "EIGHT": "E8IGHT",
    "NINE": "N9INE",
}

if __name__ == "__main__":

    with open("input", "r") as file:
        input_lines = file.read().splitlines()

    running_total = 0

    for line in input_lines:
        for num in NUMBERS.keys():
            if num in line.upper():
                line = line.upper().replace(num, NUMBERS[num])

        first_digit = next(char for char in line if char.isdigit())
        last_digit = next(char for char in reversed(line) if char.isdigit())

        line_digit = int(f"{first_digit}{last_digit}")

        running_total += line_digit

    print(f"final result was {running_total}")
