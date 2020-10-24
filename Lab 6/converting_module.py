# If value is out of range -1 is return otherwise the converted value is returned.
def milesToKm(miles):
    if miles > 0:
        kilometers = miles * 1.6
        print(str(miles) + ' Miles is equal to ' + str("%.2f" % kilometers) + ' Kilometers.')
        return kilometers
    elif miles < 0:
        return -1
# If value is out of range -1 is return otherwise the converted value is returned.
def fahToCel(fahrenheit):
    if fahrenheit <= 1000:
        celsius = ((fahrenheit - 32) * (5 / 9))
        print(str(fahrenheit) + ' Fahrenheit is equal to ' + str("%.2f" % celsius) + ' Celsius.')
        return celsius
    elif fahrenheit > 1000:
        return -1


# If value is out of range -1 is return otherwise the converted value is returned.
def galToLit(gallons):
    if gallons > 0:
        liters = gallons * 3.9
        print(str(gallons) + ' Gallons is equal to ' + str("%.2f" % liters) + ' Liters.')
        return liters
    elif gallons < 0:
        return -1


# If value is out of range -1 is return otherwise the converted value is returned.
def poundsToKg(pounds):
    if pounds > 0:
        kilograms = pounds * 0.45
        print(str(pounds) + ' Pounds is equal to ' + str("%.2f" % kilograms) + ' Kilograms.')
        return kilograms
    elif pounds < 0:
        return -1


# If value is out of range -1 is return otherwise the converted value is returned.
def inchesToCm(inches):
    if inches > 0:
        centimeters = inches * 2.54
        print(str(inches) + ' Inches is equal to ' + str("%.2f" % centimeters) + ' Centimeters.')
        return centimeters
    elif inches < 0:
        return -1

