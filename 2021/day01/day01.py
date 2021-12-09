def part_one():
    count = 0
    array = []

    f = open("input.txt", "r")
    lines = f.readlines()

    for line in lines:
        array.append(int(line))

    for i in range(0, len(array) - 1):
        if array[i + 1] > array[i]:
            count += 1

    print("Part One:", count)

def part_two():
    count = 0
    array = []

    f = open("input.txt", "r")
    lines = f.readlines()

    for line in lines:
        array.append(int(line))

    current_window = array[0] + array[1] + array[2]

    for i in range(1, len(array) - 2):
        next_window = array[i] + array[i + 1] + array[i + 2]

        if next_window > current_window:
            count += 1

        current_window = next_window

    print("Part Two:", count)

part_one()
part_two()
