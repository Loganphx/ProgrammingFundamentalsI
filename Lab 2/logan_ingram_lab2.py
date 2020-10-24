miles = float(input('Convert miles to kilometers: '))
milesToKilometers = miles*1.6
print(str(miles) + ' Miles is equal to ' + str("%.2f" % milesToKilometers) + ' Kilometers.')

fahrenheit = float(input('Convert Fahrenheit to Celsius: '))
fahrenheitToCelsius = ((fahrenheit - 32) * (5 / 9))
print(str(fahrenheit) + '° F is equal to '  + str("%.2f" % fahrenheitToCelsius) + '° C.')

gallons = float(input('Convert gallons to liters: '))
gallonsToLiters = gallons * 3.9
print(str(gallons) + ' Gallons is equal to ' + str("%.2f" % gallonsToLiters) + ' Liters.')

pounds = float(input('Convert pounds to kilograms: '))
poundsToKilograms = pounds * 0.45
print(str(pounds) + ' Pounds is equal to ' + str("%.2f" % poundsToKilograms) + ' Kilograms.')

inches = float(input('Convert inches to centimeters: '))
inchesToCentimeters = inches * 2.54
print(str(inches) + ' Inches is equal to ' + str("%.2f" % inchesToCentimeters) + ' Centimeters.')
