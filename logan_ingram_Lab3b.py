# Inputted User Values are saved as variables
name = str(input('Enter name of salesperson: '))
longevity = int(input("Enter how long they've been with the company in # of months: "))
sales = float(input('Enter # of sales in $: '))
vacationDays = int(input('Enter vacation days this month: '))

baseSalary = 2000
totalPaycheck = 0
additionalBonus = 0
commission = 0
bonus = 0
deductions = 0

# Deducts $200 from paycheck for missing 3 or more days.
if vacationDays >= 3:
    deductions = 200
# If the employee has worked at the company for 3+ months, then they are able to acquire a commission.
if longevity >= 3:
    # If the employee has made at minimum $10,000 but at maximum $100,000 in sales, then they earn a commission of 2%.
    if 10000 <= sales <= 100000:
        commission = sales * 0.02
    # If the employee has made at minimum $100,001 but at maximum $500,000 in sales, then they earn a commission of 15%.
    elif 100001 <= sales <= 500000:
        commission = sales * 0.15
        bonus = 1000
    # If the employee has made at minimum $500,001 but at maximum $1,000,000 in sales,
    # then they earm a commission of 28%.
    elif 500001 <= sales <= 1000000:
        commission = sales * 0.28
        bonus = 5000
    # If the employee has made at minimum $1,000,000, then they earn a commission of 2%.
    elif sales > 1000000:
        commission = sales * 0.35
        bonus = 100000
# Salesperson gets a $1000 bonus, if they have worked at the company for 5 or more years
# and if they have made over 100k in sales
elif longevity >= 60:
    if sales > 100000:
        additionalBonus = 1000

totalPaycheck = baseSalary + additionalBonus + commission + bonus - deductions
print('')
print('Name: ' + name)
print('Longevity: ' + str(longevity) + ' Months')
print('Base Salary: $' + str("%.2f" % baseSalary))
print('Commission: $' + str("%.2f" % commission))
print('Bonus: $' + str("%.2f" % bonus))
print('Deductions: $' + str("%.2f" % deductions))
print('Gross Pay: $' + str("%.2f" % totalPaycheck))
