with open('input.txt') as f:
    lines = f.read().split("\n")

balance = [0 for i in range(len(lines[0]))]

for binary in lines:
    for i in range(len(binary)):
        balance[i] += int(binary[i]) * 2 - 1

gamma = ""
epsilon = ""

for bit in balance:
    if bit > 0:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma + '0'
        epsilon = epsilon + '1'

gamma_dec = 0
epsilon_dec = 0
power_of_two = 1

for i in range(len(gamma) - 1, -1, -1):
    if(gamma[i] == '1'):
        gamma_dec += power_of_two
    else:
        epsilon_dec += power_of_two
    power_of_two *= 2

print(gamma_dec * epsilon_dec)
