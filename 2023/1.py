import re


if __name__ == '__main__':
    lines = [line.strip() for line in open("1_input.txt", 'r').readlines()]

    convert = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    e = "|".join(convert.keys())
    to_search = f"(?=(\d|{e}))"

    total = 0
    for line in lines:
        matches = re.findall(to_search, line)
        number1 = matches[0]
        number2 = matches[-1]
        if convert.get(number1) is not None:
            number1 = convert[number1]
        if convert.get(number2) is not None:
            number2 = convert[number2]
        total += int(number1 + number2)

    print(total)
