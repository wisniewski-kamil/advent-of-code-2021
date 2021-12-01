with open('input.txt') as f:
    lines = f.read().split("\n")

increases = 0

for i in range(3, len(lines), 1):
    if int(lines[i]) > int(lines[i - 3]):
        increases += 1

print(increases)
