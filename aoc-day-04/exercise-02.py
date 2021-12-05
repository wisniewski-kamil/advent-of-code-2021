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
won_bingos = [1 for i in range(len(bingos))]
for number in numbers:
    for i in range(len(bingos)):
        cords = contains_number(bingos[i][0], number)
        if cords:
            bingos[i][1][cords[0]][cords[1]] = 1
            if is_bingo(bingos[i][1]):
                won_bingos[i] = 0
                if sum(won_bingos) == 0:
                    answer = bingo_sum(bingos[i]) * int(number)
                    break
    if answer != 0:
        break

print(answer)
