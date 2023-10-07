# Converting JS function into Python

def maskify(cc):
    if len(cc) <= 4:
        return cc

    lastFour = cc[-4:]

    masking = '#' * (len(cc)-4)

    return masking + lastFour