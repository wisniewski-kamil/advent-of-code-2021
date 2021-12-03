with open('input.txt') as f:
    lines = f.read().split("\n")


def return_parameter(index, numbers, filter):
    balance = 0

    for binary in numbers:
        balance += int(binary[index]) * 2 - 1

    filtered = list(filter(index, numbers, balance))

    if len(filtered) == 1:
        return filtered[0]
    else:
        return return_parameter(index+1, filtered, filter)


def oxygen_filter(index, numbers, balance):
    if balance >= 0:
        return filter(lambda number: number[index] == '1', numbers)
    else:
        return filter(lambda number: number[index] == '0', numbers)


def co2_filter(index, numbers, balance):
    if balance >= 0:
        return filter(lambda number: number[index] == '0', numbers)
    else:
        return filter(lambda number: number[index] == '1', numbers)


oxygen = return_parameter(0, lines.copy(), oxygen_filter)
co2 = return_parameter(0, lines.copy(), co2_filter)

oxygen_dec = 0
co2_dec = 0
power_of_two = 1

for i in range(len(oxygen) - 1, -1, -1):
    if oxygen[i] == '1':
        oxygen_dec += power_of_two
    if co2[i] == '1':
        co2_dec += power_of_two
    power_of_two *= 2

print(oxygen_dec * co2_dec)
