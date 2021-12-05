with open('input.txt') as f:
    lines = f.read().split("\n")

numbers = lines[0].split(",")

bingos = []
bingo_index = 0
bingos.append([[],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
               ])

for line in lines[2:]:
    if line == "":
        bingo_index += 1
        bingos.append([[],
                       [[0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]
                       ])
    else:
        bingos[bingo_index][0].append(line.strip().split())


def is_bingo(bingo_table):
    for row in bingo_table:
        if sum(row) == 5:
            return True
    for i in range(5):
        if bingo_table[0][i] + bingo_table[1][i] + bingo_table[2][i] + bingo_table[3][i] + bingo_table[4][i] == 5:
            return True
    return False


def contains_number(bingo, number):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == number:
                return [i, j]
    return False


def bingo_sum(bingo_tuple):
    bingo_sum = 0
    for i in range(5):
        for j in range(5):
            if bingo_tuple[1][i][j] == 0:
                bingo_sum += int(bingo_tuple[0][i][j])
    return bingo_sum

answer = 0
for number in numbers:
    for bingo in bingos:
        cords = contains_number(bingo[0], number)
        if cords:
            bingo[1][cords[0]][cords[1]] = 1
            if is_bingo(bingo[1]):
                answer = bingo_sum(bingo) * int(number)
                break
    if answer != 0:
        break

print(answer)
