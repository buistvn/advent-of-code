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

def part_two():
    oxygen_generator_rating_binary = ""
    CO2_scrubber_rating_binary = ""
    oxygen_generator_rating_decimal = 0
    CO2_scrubber_rating_decimal = 0
    array = []
    array_oxygen = []
    array_CO2 = []

    f = open("input.txt", "r")
    lines = f.readlines()

    for line in lines:
        array.append(line.strip())

    array_oxygen = array
    array_CO2 = array

    for i in range(0, len(array[0])):
        if len(array_oxygen) > 1:
            count_zero = len([x for x in array_oxygen if x[i] == "0"])
            count_one = len([x for x in array_oxygen if x[i] == "1"])

            if count_one >= count_zero:
                array_oxygen = [x for x in array_oxygen if x[i] == "1"]
            else:
                array_oxygen = [x for x in array_oxygen if x[i] == "0"]

        if len(array_CO2) > 1:
            count_zero = len([x for x in array_CO2 if x[i] == "0"])
            count_one = len([x for x in array_CO2 if x[i] == "1"])

            if count_one >= count_zero:
                array_CO2 = [x for x in array_CO2 if x[i] == "0"]
            else:
                array_CO2 = [x for x in array_CO2 if x[i] == "1"]

    oxygen_generator_rating_binary = array_oxygen[0]
    CO2_scrubber_rating_binary = array_CO2[0]

    oxygen_generator_rating_decimal = int(oxygen_generator_rating_binary, 2)
    CO2_scrubber_rating_decimal = int(CO2_scrubber_rating_binary, 2)

    print("Part Two:", oxygen_generator_rating_decimal * CO2_scrubber_rating_decimal)

part_one()
part_two()
