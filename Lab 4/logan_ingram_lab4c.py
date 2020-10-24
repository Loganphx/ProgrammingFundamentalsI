i = 0
grades = []
totalGrades = 0
#Program loops until the user enters -1, which ends the inputting of grades
while i != -1:
    grade = float(input('Enter student grade: '))
    # If value is out of bounds, the program will exit.
    if(grade == -1):
        i = -1
    # Otherwise it will calculate the grade letter and add up all entered grades
    else:
        if(90.0 <= grade <= 100):
            print('A... Awesome!')
        elif(80 <= grade < 90):
            print('B... Not Bad')
        elif(70 <= grade < 80):
            print('C... Curiously bad')
        elif(60 <= grade < 70):
            print('D... Not Decent.')
        elif(0 <= grade < 60):
            print('F... You are a failure.')
        grades.append(grade)
        totalGrades+=grade
#If grades have been entered, then the average will be calculated and outputted
if(len(grades) > 0):
    print('Class Average: ' + str(totalGrades/len(grades)))
else:
    print('No grades were entered.')