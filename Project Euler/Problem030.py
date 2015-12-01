from math import log10

def digit_powers(exponent):
    if exponent <= 1:
        return "The exponent must be at least 2."
    # Get the powers
    powers = [i ** exponent for i in range(10)]
    answer = 0
    limit = (exponent + 1) * (9 ** exponent)
    # Search for them
    for i in range(10, limit):
        savei = i
        total = 0
        for _ in range(int(log10(i)) + 1):
            digit = i % 10
            total += powers[digit]
            i //= 10

        if (total == savei):
            answer += total
    return answer

print(digit_powers(5))