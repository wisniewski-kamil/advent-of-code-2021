with open('input.txt') as f:
    lines = f.read().split("\n")

hor = 0
dep = 0
aim = 0

for command in lines:
    command_text = command.split(" ")[0]
    command_value = command.split(" ")[1]

    if command_text == "forward":
        hor += int(command_value)
        dep += int(command_value) * aim
    elif command_text == "up":
        aim -= int(command_value)
    else:
        aim += int(command_value)

print(hor * dep)
