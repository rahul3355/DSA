def leapYear(year):
    if year % 4 == 0 and (year<1918 or year % 400 == 0 or year % 100 != 0):
        return True 
    else:
        return False


def dayOfProgrammer(year):
    # Write your code here
    if leapYear(year):
        x = "12.09." + str(year)
        return x
    else:
        if year != 1918:
            x = "13.09." + str(year)
            return x
        else:
            x = "26.09." + str(year)
            return x