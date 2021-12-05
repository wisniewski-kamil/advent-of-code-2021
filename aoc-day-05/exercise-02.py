with open('input.txt') as f:
    lines = f.read().split("\n")

lines_split = []
for line in lines:
    lines_split.append(line.split(" -> "))

list_of_cords = []
for pair in lines_split:
    list_of_cords.append([pair[0].split(","), pair[1].split(",")])


def add(x, y, diag):
    if diag.get(str(x) + "," + str(y)) != None:
        diag[str(x) + "," + str(y)] += 1
    else:
        diag[str(x) + "," + str(y)] = 1


diagram = {}

for cords in list_of_cords:
    if cords[0][0] == cords[1][0]:
        if int(cords[0][1]) > int(cords[1][1]):
            for i in range(int(cords[1][1]), int(cords[0][1]) + 1):
                add(int(cords[0][0]), i, diagram)
        else:
            for i in range(int(cords[0][1]), int(cords[1][1]) + 1):
                add(int(cords[0][0]), i, diagram)
    elif cords[0][1] == cords[1][1]:
        if int(cords[0][0]) > int(cords[1][0]):
            for i in range(int(cords[1][0]), int(cords[0][0]) + 1):
                add(i, int(cords[0][1]), diagram)
        else:
            for i in range(int(cords[0][0]), int(cords[1][0]) + 1):
                add(i, int(cords[0][1]), diagram)
    else:
        length = abs(int(cords[0][0]) - int(cords[1][0])) + 1
        diagonal_cords = [[0, 0] for i in range(length)]
        if int(cords[0][1]) < int(cords[1][1]):
            for i in range(int(cords[0][1]), int(cords[1][1]) + 1):
                diagonal_cords[i - int(cords[0][1])][1] = i
        else:
            for i in range(int(cords[0][1]), int(cords[1][1]) - 1, -1):
                diagonal_cords[int(cords[0][1]) - i][1] = i
        if int(cords[0][0]) < int(cords[1][0]):
            for i in range(int(cords[0][0]), int(cords[1][0]) + 1):
                diagonal_cords[i - int(cords[0][0])][0] = i
        else:
            for i in range(int(cords[0][0]), int(cords[1][0]) - 1, -1):
                diagonal_cords[int(cords[0][0]) - i][0] = i
        for cord in diagonal_cords:
            add(cord[0], cord[1], diagram)

counter = 0
for key in diagram:
    if diagram[key] > 1:
        counter += 1

print(counter)
