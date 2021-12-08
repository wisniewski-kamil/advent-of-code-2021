with open('input.txt') as f:
    lines = f.read().split("\n")

signals = [line.split(" | ") for line in lines]


def contains(b, a):
    for letter in a:
        if letter not in b:
            return False
    return True


def decode_digits(key):
    digits = ["" for i in range(10)]

    for n in key:
        if len(n) == 2:
            digits[1] = n
        elif len(n) == 4:
            digits[4] = n
        elif len(n) == 3:
            digits[7] = n
        elif len(n) == 7:
            digits[8] = n

    key.remove(digits[1])
    key.remove(digits[4])
    key.remove(digits[7])
    key.remove(digits[8])

    for n in key:
        if len(n) == 5 and contains(n, digits[7]):
            digits[3] = n
        elif len(n) == 6 and contains(n, digits[4]):
            digits[9] = n

    key.remove(digits[3])
    key.remove(digits[9])

    for n in key:
        if len(n) == 6 and contains(n, digits[1]):
            digits[0] = n
        elif len(n) == 5 and contains(digits[9], n):
            digits[5] = n

    key.remove(digits[0])
    key.remove(digits[5])

    if len(key[0]) == 5:
        digits[2] = key[0]
        digits[6] = key[1]
    else:
        digits[2] = key[1]
        digits[6] = key[0]

    return digits


def transfer(coded, key):
    for i in range(10):
        if len(key[i]) == len(coded) and contains(key[i], coded):
            return i


answer = 0

for signal in signals:
    inp = signal[0].split()
    output = signal[1].split()

    digits = decode_digits(inp)

    decoded_output = ""
    for n in output:
        decoded_output += str(transfer(n, digits))

    answer += int(decoded_output)

print(answer)
