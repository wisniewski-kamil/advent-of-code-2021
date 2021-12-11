with open('input.txt') as f:
    lines = f.read().split("\n")

answer = 0

for r in range(len(lines)):
    for c in range(len(lines[0])):
        up = r - 1 if r > 0 else r + 1
        down = r + 1 if r < len(lines) - 1 else r - 1
        left = c - 1 if c > 0 else c + 1
        right = c + 1 if c < len(lines[0]) - 1 else c - 1

        if int(lines[r][c]) < int(lines[up][c]) and int(lines[r][c]) < int(lines[down][c]) and int(lines[r][c]) < int(lines[r][left]) and int(lines[r][c]) < int(lines[r][right]):
            answer += 1 + int(lines[r][c])

print(answer)
