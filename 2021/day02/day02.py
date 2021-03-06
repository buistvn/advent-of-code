def part_one():
    horizontal_position = 0
    depth = 0
    directions = []
    units = []

    f = open("input.txt", "r")
    lines = f.readlines()

    for line in lines:
        command = line.split()
        directions.append(command[0])
        units.append(int(command[1]))

    for i in range(0, len(lines)):
        if directions[i] == "forward":
            horizontal_position += units[i]
        elif directions[i] == "down":
            depth += units[i]
        elif directions[i] == "up":
            depth -= units[i]

    print("Part One:", horizontal_position * depth)

def part_two():
    horizontal_position = 0
    depth = 0
    aim = 0
    directions = []
    units = []

    f = open("input.txt", "r")
    lines = f.readlines()

    for line in lines:
        command = line.split()
        directions.append(command[0])
        units.append(int(command[1]))

    for i in range(0, len(lines)):
        if directions[i] == "forward":
            horizontal_position += units[i]
            depth += (aim * units[i])
        elif directions[i] == "down":
            aim += units[i]
        elif directions[i] == "up":
            aim -= units[i]

    print("Part Two:", horizontal_position * depth)

part_one()
part_two()
