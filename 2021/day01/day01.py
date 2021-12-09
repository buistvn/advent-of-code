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

part_one()
