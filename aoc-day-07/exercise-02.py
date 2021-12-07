import statistics

with open('input.txt') as f:
    numbers = f.read().split(",")

numbers_int = [int(n) for n in numbers]

minimum = min(numbers_int)
maximum = max(numbers_int)

med = int(statistics.median(numbers_int))

med_dist = 0
med_minus_one_dist = 0
for n in numbers_int:
    med_dist += (abs(n - med) + 1) * (abs(n - med) / 2)
    med_minus_one_dist += (abs(n - (med - 1)) + 1) * (abs(n - (med - 1)) / 2)

dif = -1 if med_minus_one_dist < med_dist else 1

prev = med_dist if med_minus_one_dist < med_dist else med_minus_one_dist
next = med_minus_one_dist if med_minus_one_dist < med_dist else med_dist
position = med - 1 if med_minus_one_dist < med_dist else med

while prev > next:
    prev = next
    next = 0
    position += dif
    for n in numbers_int:
        next += (abs(n - position) + 1) * (abs(n - position) / 2)

print(int(prev))
