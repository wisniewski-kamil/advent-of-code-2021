with open('input.txt') as f:
    lines = f.read().split("\n")

hor = 0
dep = 0

for command in lines:
    command_text = command.split(" ")[0]
    command_value = command.split(" ")[1]

    if command_text == "forward":
        hor += int(command_value)
    elif command_text == "up":
        dep -= int(command_value)
    else:
        dep += int(command_value)

print(hor * dep)
