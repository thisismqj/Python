def average(l):
    adder = 0.0
    for each in l:
        adder += each
    return adder / len(l)

def variance(l):
    ave = average(l)
    adder = 0.0
    for each in l:
        adder += (each - ave)**2
    return adder / len(l)
