import statistics

with open('input.txt') as f:
    numbers = f.read().split(",")

numbers_int = [int(n) for n in numbers]

position = int(statistics.median(numbers_int))

fuel = 0

for n in numbers_int:
    fuel += abs(n - position)

print(fuel)
