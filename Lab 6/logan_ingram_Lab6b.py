def main():
    try:
        # Opens grade.txt file.
        gradesFile = open('grades.txt', 'a')

        # Loops 12 times taking grades each time
        for i in range(0, 12):
            try:
                studentGrade = 0
                # Gets student name and average grade from user.
                studentName = input("Enter student's name: ")
                studentGrade = float(input("Enter student's average grade: "))

                if studentGrade < 0 or studentGrade > 100:
                    # Raises exception if student Grade is out of range.
                    raise Exception
                else:
                    # Student name and average are written to grades.txt
                    gradesFile.writelines(studentName + ', ' + str(studentGrade) + '\n')

            # If an exception occurs, an ERROR is displayed depending why the exception occurred.
            except Exception:
                if float(studentGrade):
                    if studentGrade < 0:
                        print('ERROR: Student grade must be greater than 0.')
                    elif studentGrade > 100:
                        print('ERROR: Student grade cannot be greater than 100.')
                else:
                    print('ERROR: Student Grade must be a numerical value.')
        # gradesFile is closed to prevent memory leaks.
        gradesFile.close()

    except Exception:
        print('ERROR: grades.txt could not be created.')
    try:
        fileName = 'grades.txt'
        # Attempts to open grades.txt file
        gradesFile = open(fileName, 'r')
        lines = gradesFile.readlines()

        # Reads each line from gradesFile and outputs it.
        for line in lines:
            tempArray = line.split(',')
            tempName = tempArray[0]
            tempGrade = tempArray[1].split('\n')[0]
            print(tempName + ',' + tempGrade)

        # gradesFile is closed to prevent a memory leak.
        gradesFile.close()

    except FileNotFoundError:
        # If file is not found then an exception occurs where the user is prompted for the proper file name.
        print('File by the name of ' + fileName + ' not found.')

        fileName = input('Enter the correct name of the file: ')
        try:
            gradesFile = open(fileName, 'r')
            lines = gradesFile.readlines()
            for line in lines:
                tempArray = line.split(',')
                tempName = tempArray[0]
                tempGrade = tempArray[1].split('\n')[0]
                print(tempName + ',' + tempGrade)
            # gradesFile is closed to prevent a memory leak.
            gradesFile.close()

        except FileNotFoundError:
            print('No file by that name exists.')


# Calls the main function.
main()
