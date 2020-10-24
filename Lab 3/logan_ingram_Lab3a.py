# User inputs Miles as a decimal value.
miles = float(input('Convert miles to kilometers: '))
# If the value is acceptable continue, otherwise end program
if miles > 0:
    kilometers = miles*1.6
    print(str(miles) + ' Miles is equal to ' + str("%.2f" % kilometers) + ' Kilometers.')
    fahrenheit = float(input('Convert Fahrenheit to Celsius: '))
    if fahrenheit <= 1000:
        celsius = ((fahrenheit - 32) * (5 / 9))
        print(str(fahrenheit) + '° F is equal to ' + str("%.2f" % celsius) + '° C.')
        gallons = float(input('Convert gallons to liters: '))
        if gallons > 0:
            liters = gallons * 3.9
            print(str(gallons) + ' Gallons is equal to ' + str("%.2f" % liters) + ' Liters.')
            pounds = float(input('Convert pounds to kilograms: '))
            if pounds > 0:
                kilograms = pounds * 0.45
                print(str(pounds) + ' Pounds is equal to ' + str("%.2f" % kilograms) + ' Kilograms.')
                inches = float(input('Convert inches to centimeters: '))
                if inches > 0:
                    centimeters = inches * 2.54
                    print(str(inches) + ' Inches is equal to ' + str("%.2f" % centimeters) + ' Centimeters.')
                else:
                    print('Inches must be greater than 0.')
            else:
                print('ERROR: Pounds must be greater than 0.')
        else:
            print('ERROR: Gallons must be greater than 0')
    else:
        print('ERROR: Temperature cannot be greater than 1000 F°')
else:
    print('ERROR: Miles must be greater than 0')
