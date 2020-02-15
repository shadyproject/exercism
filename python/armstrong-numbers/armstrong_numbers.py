def is_armstrong(number):
    sum = 0
    exponent = len(str(number))
    for n in str(number):
        sum += (int(n) ** exponent)

    return sum == number
