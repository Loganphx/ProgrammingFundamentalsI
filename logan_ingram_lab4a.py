def milesToKm(miles):
    if miles > 0:
        kilometers = miles * 1.6
        print(str(miles) + ' Miles is equal to ' + str("%.2f" % kilometers) + ' Kilometers.')
        return kilometers
    elif miles < 0:
        return -1


def fahToCel(fahrenheit):
    if fahrenheit <= 1000:
        celsius = ((fahrenheit - 32) * (5 / 9))
        print(str(fahrenheit) + ' Fahrenheit is equal to ' + str("%.2f" % celsius) + ' Celsius.')
        return celsius
    elif fahrenheit > 1000:
        return -1


def galToLit(gallons):
    if gallons > 0:
        liters = gallons * 3.9
        print(str(gallons) + ' Gallons is equal to ' + str("%.2f" % liters) + ' Liters.')
        return liters
    elif gallons < 0:
        return -1


def poundsToKg(pounds):
    if pounds > 0:
        kilograms = pounds * 0.45
        print(str(pounds) + ' Pounds is equal to ' + str("%.2f" % kilograms) + ' Kilograms.')
        return kilograms
    elif pounds < 0:
        return -1


def inchesToCm(inches):
    if inches > 0:
        centimeters = inches * 2.54
        print(str(inches) + ' Inches is equal to ' + str("%.2f" % centimeters) + ' Centimeters.')
        return centimeters
    elif inches < 0:
        return -1


def main():
    a = 0
    # User is given three attempts to enter a valid number of miles, otherwise the program errors and exits.
    while a < 3:
        miles = float(input('Convert Miles to Kilometers: '))
        kilometers = milesToKm(miles)
        if kilometers != -1:
            a = 3
            b = 0
            # User is given three attempts to enter a valid number of fahrenheit, otherwise the program errors and exits.
            while b < 3:
                fahrenheit = float(input('Convert Fahrenheit to Celsius: '))
                celsius = fahToCel(fahrenheit)
                if celsius != -1:
                    b = 3
                    c = 0
                    # User is given three attempts to enter a valid number of gallons, otherwise the program errors and exits.
                    while c < 3:
                        gallons = float(input('Convert gallons to liters: '))
                        liters = galToLit(gallons)
                        if liters != -1:
                            c = 3
                            d = 0
                            # User is given three attempts to enter a valid number of pounds, otherwise the program errors and exits.
                            while d < 3:
                                pounds = float(input('Convert pounds to kilograms: '))
                                kilograms = poundsToKg(pounds)
                                if kilograms != -1:
                                    d = 3
                                    e = 0
                                    # User is given three attempts to enter a valid number of inches, otherwise the program errors and exits.
                                    while e < 3:
                                        inches = float(input('Convert inches to centimeters: '))
                                        centimeters = inchesToCm(inches)
                                        if centimeters != -1:
                                            e = 3
                                        if centimeters == -1 and e != 2:
                                            e += 1
                                            print('ERROR: Inches must be greater than 0.')
                                        elif centimeters == -1 and e == 2:
                                            e = 3
                                            print("You were given three attempts and you failed.")
                                            print("So the program will exit.")
                                elif kilograms == -1 and d != 2:
                                    d += 1
                                    print('ERROR: Pounds must be greater than 0.')
                                elif kilograms == -1 and d == 2:
                                    d = 3
                                    print("You were given three attempts and you failed.")
                                    print("So the program will exit.")
                        elif liters == -1 and c != 2:
                            c += 1
                            print('ERROR: Gallons must be greater than 0.')
                        elif liters == -1 and c == 2:
                            c = 3
                            print("You were given three attempts and you failed.")
                            print("So the program will exit.")

                elif celsius == -1 and b != 2:
                    b += 1
                    print('ERROR: Fahrenheit must be greater than 0.')
                elif celsius == -1 and b == 2:
                    b = 3
                    print("You were given three attempts and you failed.")
                    print("So the program will exit.")
        elif kilometers == -1 and a != 2:
            a += 1
            print('ERROR: Miles must be greater than 0.')
        elif kilometers == -1 and a == 2:
            a = 3
            print("You were given three attempts and you failed.")
            print("So the program will exit.")


main()
