sum = 0
coffeeInventory = open('coffeeInventory.txt', 'r')
lines = coffeeInventory.readlines()
for line in lines:
    print(line)
    sum += int(line.split(',')[1].split('\n')[0][1:])
print('Total Pounds of Coffee, ' + str(sum))
coffeeInventory.close()

coffeeInventory = open('coffeeInventory.txt', 'a')
coffeeInventory.writelines('Guatemala Antigua, 22\n')
coffeeInventory.writelines('House Blend, 25\n')
coffeeInventory.writelines('Decaf House Blend, 16\n')
coffeeInventory.close()

coffeeInventory = open('coffeeInventory.txt', 'r')
print(coffeeInventory.readlines())
try:
    description = input('Description of coffee to remove: ')

except Exception:
    print('Error Occured.')