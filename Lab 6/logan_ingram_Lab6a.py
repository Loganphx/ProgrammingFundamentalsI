#Imports Converting_Module which contains all functions used for the program
from converting_module import *

def main():
    # Opens filed named conversions.txt
    conversionFile = open('conversions.txt', 'a')
    print('Conversions')
    print('a. Miles to Kilometers'
          '\nb. Gallons to Liters'
          '\nc. Pounds to Kilograms'
          '\nd. Inches to Centimeters'
          '\ne. Fahrenheit to Celsius')

    try:
        option = input('Select an option: ')
        # User is given three attempts to enter a value greater than 0
        if option == 'a':
            # Loops ten times
            for x in range(0,10):
                a = 0
                while a < 3:
                    try:
                        # Gets the number of miles to convert
                        miles = float(input('Convert Miles to Kilometers: '))
                        kilometers = milesToKm(miles)
                        if kilometers != -1:
                            a = 3
                            # Writes conversion data to conversion.txt
                            conversionFile.writelines(str(miles) + '\t Miles \t' + str(kilometers) + '\t Kilometers \n')
                        elif kilometers == -1:
                            a += 1
                            raise ValueError

                    except ValueError:
                        try:
                            if a == 3:
                                print("You were given three attempts and you failed.")
                                print("So the program will exit.")
                            elif type(miles) is float:
                                if a != 3:
                                    print('ERROR: Miles must be greater than 0.')
                            else:
                                raise Exception
                        except Exception:
                            print('Miles must be a numerical value.')
        elif option == 'b':
            # Loops ten times
            for x in range(0,10):
                a = 0
                # User is given three attempts to enter a valid number of gallons, otherwise the program errors and exits.
                while a < 3:
                    try:
                        # Get the gallons from user
                        gallons = float(input('Convert gallons to liters: '))
                        liters = galToLit(gallons)
                        if liters != -1:
                            a = 3
                            # Writes conversion data to conversion.txt
                            conversionFile.writelines(str(gallons) + '\t Gallons \t' + str(liters) + '\t Liters \n')
                        elif liters == -1:
                            a += 1
                            raise ValueError

                    except ValueError:
                        try:
                            if a == 3:
                                print("You were given three attempts and you failed.")
                                print("So the program will exit.")
                            elif type(gallons) is float:
                                if a != 3:
                                    print('ERROR: Gallons must be greater than 0.')
                            else:
                                raise Exception
                        except Exception:
                            print('Gallons must be a numerical value.')
        elif option == 'c':
            # Loops ten times
            for x in range(0, 10):
                a = 0
                # User is given three attempts to enter a valid number of pounds, otherwise the program errors and exits.
                while a < 3:
                    try:
                        # Get the pounds from user
                        pounds = float(input('Convert pounds to kilograms: '))
                        kilograms = poundsToKg(pounds)
                        if kilograms != -1:
                            a = 3
                            # Writes conversion data to conversion.txt
                            conversionFile.writelines(str(pounds) + '\t Pounds \t' + str(kilograms) + '\t Kilograms \n')
                        elif kilograms == -1:
                            a += 1
                            raise ValueError

                    except ValueError:
                        try:
                            if a == 3:
                                print("You were given three attempts and you failed.")
                                print("So the program will exit.")
                            elif type(pounds) is float:
                                if a != 3:
                                    print('ERROR: Pounds must be greater than 0.')
                            else:
                                raise Exception
                        except Exception:
                            print('Pounds must be a numerical value.')

        elif option == 'd':
            # Loops ten times
            for x in range(0,10):
                a = 0
                # User is given three attempts to enter a valid number of inches, otherwise the program errors and exits.
                while a < 3:
                    try:
                        # Get the inches from user
                        inches = float(input('Convert inches to centimeters: '))
                        centimeters = inchesToCm(inches)
                        if centimeters != -1:
                            a = 3
                            # Writes conversion data to conversion.txt
                            conversionFile.writelines(str(inches) + '\t Inches \t' + str(centimeters) + '\t Centimeters \n')
                        elif centimeters == -1:
                            a += 1
                            raise ValueError
                    except ValueError:
                        try:
                            if a == 3:
                                print("You were given three attempts and you failed.")
                                print("So the program will exit.")
                            elif type(inches) is float:
                                if a != 3:
                                    print('ERROR: Inches must be greater than 0.')
                            else:
                                raise Exception
                        except Exception:
                            print('Inches must be a numerical value.')
        elif option == 'e':
            # Loops ten times
            for x in range(0,10):
                a = 0
                # User is given three attempts to enter a valid number of fahrenheit, otherwise the program errors and exits.
                while a < 3:
                    try:
                        # Get the degrees of fahrenheit from user
                        fahrenheit = float(input('Convert Fahrenheit to Celsius: '))
                        celsius = fahToCel(fahrenheit)
                        if celsius != -1:
                            a = 3
                            # Writes conversion data to conversion.txt
                            conversionFile.writelines(str(fahrenheit) + '\t Fahrenheit \t' + str(celsius) + '\t Celsius \n')
                        elif celsius == -1:
                            a += 1
                            raise ValueError

                    except ValueError:
                        try:
                            if a == 3:
                                print("You were given three attempts and you failed.")
                                print("So the program will exit.")
                            elif type(fahrenheit) is float:
                                if a != 3:
                                    print('ERROR: Fahrenheit cannot be greater than 1000°.')
                            else:
                                raise Exception
                        except Exception:
                            print('Fahrenheit must be a numerical value.')
        else:
            raise KeyError
    except KeyError:
        print('ERROR: Choose a proper option')

    #Closes the file.
    conversionFile.close()



# Calls the main function.
main()
