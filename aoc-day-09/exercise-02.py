with open('input.txt') as f:
    lines = f.read().split("\n")

visited = [[True if int(n) == 9 else False for n in lines[i]] for i in range(len(lines))]


def get_size(a, b, visits):
    count = 0
    que = [[a, b]]
    visits[a][b] = True

    while que:
        current = que.pop(0)
        x = current[0]
        y = current[1]
        count += 1

        if x > 0 and not visits[x - 1][y]:
            que.append([x - 1, y])
            visits[x - 1][y] = True
        if x < len(visits) - 1 and not visits[x + 1][y]:
            que.append([x + 1, y])
            visits[x + 1][y] = True
        if y > 0 and not visits[x][y - 1]:
            que.append([x, y - 1])
            visits[x][y - 1] = True
        if y < len(visits[0]) - 1 and not visits[x][y + 1]:
            que.append([x, y + 1])
            visits[x][y + 1] = True

    return count


first = 0
second = 0
third = 0

for r in range(len(lines)):
    for c in range(len(lines[0])):
        up = r - 1 if r > 0 else r + 1
        down = r + 1 if r < len(lines) - 1 else r - 1
        left = c - 1 if c > 0 else c + 1
        right = c + 1 if c < len(lines[0]) - 1 else c - 1

        if (int(lines[r][c]) < int(lines[up][c]) and int(lines[r][c]) < int(lines[down][c])
                and int(lines[r][c]) < int(lines[r][left]) and int(lines[r][c]) < int(lines[r][right])):
            size = get_size(r, c, visited)

            if size >= first:
                third, second, first = second, first, size
            elif size >= second:
                third, second = second, size
            elif size >= third:
                third = size

print(first * second * third)
