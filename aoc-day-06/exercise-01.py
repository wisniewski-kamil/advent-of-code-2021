with open('input.txt') as f:
    numbers = f.read().split(",")

memory = {}


def calculate(value, days, mem):
    if value >= days:
        return 0
    else:
        if mem.get(str(value) + "," + str(days)) is not None:
            return mem[str(value) + "," + str(days)]
        else:
            basic_outcome = 1 + (days - value - 1) // 7
            children_days = []
            for i in range(basic_outcome):
                children_days.append(days - value - 1 - (i * 7))
            outcome = 0
            outcome += basic_outcome
            for day in children_days:
                outcome += calculate(8, day, mem)
            mem[str(value) + "," + str(days)] = outcome
            return outcome


answer = 0
for n in numbers:
    answer += calculate(int(n), 80, memory) + 1
print(answer)
