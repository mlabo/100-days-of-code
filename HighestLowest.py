def high_and_low(numbers):
    l = [int(s) for s in numbers.split(' ')]
    high = str(max(l))  
    low = str(min(l))
    solution = "%s %s" % (high, low)
    return solution