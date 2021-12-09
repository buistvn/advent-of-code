def part_one():
    gamma_rate_binary = ""
    epsilon_rate_binary = ""
    gamma_rate_decimal = 0
    epsilon_rate_decimal = 0
    array = []

    f = open("input.txt", "r")
    lines = f.readlines()

    for line in lines:
        array.append(line.strip())

    for i in range(0, len(array[0])):
        count_zero = 0
        count_one = 0
        
        for j in range(0, len(array)):
            if array[j][i] == "0":
                count_zero += 1
            elif array[j][i] == "1":
                count_one += 1

        if count_zero > count_one:
            gamma_rate_binary += "0"
            epsilon_rate_binary += "1"
        else:
            gamma_rate_binary += "1"
            epsilon_rate_binary += "0"

    gamma_rate_decimal = int(gamma_rate_binary, 2)
    epsilon_rate_decimal = int(epsilon_rate_binary, 2)

    print("Part One:", gamma_rate_decimal * epsilon_rate_decimal)

part_one()
