def catAndMouse(x, y, z):
    distanceA = (x - z) ** 2
    distanceB = (y - z) ** 2
    if distanceA > distanceB:
        return "Cat B"
    elif distanceB > distanceA:
        return "Cat A"
    else:
        return "Mouse C"