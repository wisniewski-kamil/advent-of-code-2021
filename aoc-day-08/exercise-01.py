with open('input.txt') as f:
    lines = f.read().split("\n")

signals = [line.split(" | ")[1].split(" ") for line in lines]

counter = 0
for signal in signals:
    for s in signal:
        if len(s) in [2, 3, 4, 7]:
            counter += 1

print(counter)
