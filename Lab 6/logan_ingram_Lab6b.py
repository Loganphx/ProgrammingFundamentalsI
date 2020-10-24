def main():
    # Opens grade.txt file.
    gradesFile = open('grades.txt', 'a')
    # Loops 12 times taking grades each time
    for i in range(0, 12):
        try:
            studentGrade = 0
            studentName = input("Enter student's name: ")
            studentGrade = float(input("Enter student's average grade: "))
            if studentGrade < 0 or studentGrade > 100:
                # Raises exception if student Grade is out of range.
                raise Exception
            else:
                # Student name and average are written to grades.txt
                gradesFile.writelines(studentName + ', ' + str(studentGrade) + '\n')
        except Exception:
            if float(studentGrade):
                if studentGrade < 0:
                    print('ERROR: Student grade must be greater than 0.')
                elif studentGrade > 100:
                    print('ERROR: Student grade cannot be greater than 100.')
            else:
                print('ERROR: Student Grade must be a numerical value.')
    gradesFile.close()

    try:
        fileName = 'grades.txt'
        # Attempts to open grades.txt file
        gradesFile = open(fileName, 'r')
        lines = gradesFile.readlines()
        # Reads each line from file and prints it.
        for line in lines:
            tempArray = line.split(',')
            tempName = tempArray[0]
            tempGrade = tempArray[1].split('\n')[0]
            print(tempName + ',' + tempGrade)
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
        except FileNotFoundError:
            print('No file by that name exists.')

main()