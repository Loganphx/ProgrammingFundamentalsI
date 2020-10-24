def main():
    sum = 0
    coffeeDict = {}

    try:
        # Opens file and reads all lines
        coffeeInventory = open('coffeeInventory.txt', 'r')
        lines = coffeeInventory.readlines()

        # Splits each line by commas and then adds all items to a dictionary to prevent duplicates.
        for line in lines:
            coffeeInfo = line.split(',')
            coffeeName = coffeeInfo[0]
            if coffeeName not in coffeeDict:
                coffeeAmount = float(coffeeInfo[1].split('\n')[0][1:])
                coffeeDict[coffeeName] = coffeeAmount
                sum += float(coffeeAmount)

        # Outputs Coffee Inventory.
        for item in coffeeDict:
            print(item + ', ' + str(coffeeDict[item]))

        print('\nTotal Pounds of Coffee: ' + str(sum) + '\n')

        # Opens coffeeInventory.txt and adds three blends of coffee to the dictionary and text file.
        coffeeInventory = open('coffeeInventory.txt', 'a')
        coffeeInventory.writelines('Guatemala Antigua, 22\n')
        coffeeInventory.writelines('House Blend, 25\n')
        coffeeInventory.writelines('Decaf House Blend, 16\n')

        coffeeDict['Guatemala Antigua'] = 22
        coffeeDict['House Blend'] = 25
        coffeeDict['Decaf House Blend'] = 16

        # Closes file to prevent memory leaks.
        coffeeInventory.close()

    # FileNotFoundError occurs if the coffeeInventory file does not exist, and an ERROR is displayed.
    except FileNotFoundError:
        print('ERROR: File not found.')

    try:
        # Prints all options of blends that can be removed.
        for item in coffeeDict:
            print(item)

        # Gets user input for which blend to remove.
        description = input('\nSelect a coffee to remove: ')

        # If descriptions exists in the coffeeInventory file, then it is removed.
        if description in coffeeDict:
            coffeeDict.pop(description)
            print('Successfully removed.\n')
            coffeeInventory = open('coffeeInventory.txt', 'w')

            for item in coffeeDict:
                coffeeInventory.writelines(item + ', ' + str(coffeeDict[item]) + '\n')

            # Closes file to prevent memory leaks.
            coffeeInventory.close()

        else:
            print('That item was not found in the file.')

    except Exception:
        print('ERROR: Something went wrong.')

    try:
        # Displays options of coffee that can be replaced.
        for item in coffeeDict:
            print(item)

        # Gets which coffee to replace from user.
        description = input('\nDescription of coffee to replace: ')

        # If description exists then it is replaced by newName and newAmount.
        if description in coffeeDict:
            coffeeDict.pop(description)

            # Gets new coffee name to replace old one.
            newName = input('New Coffee Name: ')

            # If newName already exists in the file then the amount is just added instead of overriding it.
            if newName in coffeeDict:
                newAmount = float(input('New Coffee Amount: '))
                coffeeDict[newName] = coffeeDict[newName] + newAmount
            else:
                newAmount = float(input('New Coffee Amount: '))
                coffeeDict[newName] = newAmount

            coffeeInventory = open('coffeeInventory.txt', 'w')

            for item in coffeeDict:
                coffeeInventory.writelines(item + ', ' + str(coffeeDict[item]) + '\n')

            # Closes file to prevent memory leaks.
            coffeeInventory.close()
        else:
            print('That item was not found in the file.')

    # ValueError occurs if user does not enter a float value for newAmount, and an ERROR is displayed.
    except ValueError:
        print('\nERROR: You did not enter a float value.')

# Calls main function.
main()