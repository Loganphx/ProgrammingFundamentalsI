def getFahToCelRange(range):
    totalConversionsList = []
    for fahrenheit in range:
        celsius = ((fahrenheit - 32) * (5 / 9))
        conversionList = [fahrenheit, celsius]
        totalConversionsList.append(conversionList)
    return totalConversionsList

def getMilToKilometerRange(range):
    totalConversionsList = []
    for miles in range:
        kilometers = miles * 1.6
        conversionList = [miles, kilometers]
        totalConversionsList.append(conversionList)
    return totalConversionsList

def getGalToLitRange(range):
    totalConversionsList = []
    for gallons in range:
        liters = gallons * 3.9
        conversionList = [gallons, liters]
        totalConversionsList.append(conversionList)
    return totalConversionsList

def getPoundsToKgRange(range):
    totalConversionsList = []
    for pounds in range:
        kilograms = pounds * 0.45
        conversionList = [pounds, kilograms]
        totalConversionsList.append(conversionList)
    return totalConversionsList

def getInchesToCmRange(range):
    totalConversionsList = []
    for inches in range:
        centimeters = inches * 2.54
        convertionList = [inches, centimeters]
        totalConversionsList.append(convertionList)
    return totalConversionsList
def main():

    fahtoCelRange = [-10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    print('Fahrenheit to Celsius: ')
    print('\t' + str(getFahToCelRange(fahtoCelRange)))

    range = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print('Miles to Kilometers: ' + '\n' + '\t' + str(getMilToKilometerRange(range)))
    print('Gallons to Liters: ' + '\n' + '\t' + str(getGalToLitRange(range)))
    print('Pounds To Kilograms: ' + '\n' + '\t' + str(getPoundsToKgRange(range)))
    print('Inches to Centimeters: ' + '\n' + '\t' + str(getInchesToCmRange(range)))

main()