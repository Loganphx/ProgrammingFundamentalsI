def getStudentNames():
    studentsList = []
    for i in range(0,12):
        print(i)
        studentName = str(input("Enter the student's name: "))
        studentsList.append(studentName)
    return studentsList


def getAlphabeticalList(tempList):
    tempList.sort
    alphabeticalList = tempList
    return alphabeticalList


def getReverseList(tempList):
    tempList.reverse()
    reversedList = tempList
    return reversedList


def writeListToFile(tempList, fileName):
    writtenFile = open(fileName, 'w')
    for item in tempList:
        writtenFile.write(item + '\n')
    writtenFile.close()


def readListFromFile(fileName):
    readFile = open(fileName, 'r')
    tempList = readFile.readlines()
    readList = []
    for item in tempList:
        readList.append(item.split('\n')[0])
    return readList


def main():
    studentsList = getStudentNames()
    studentsList = getAlphabeticalList(studentsList)
    studentsList = getReverseList(studentsList)
    studentsList.append('Rene Polanco')
    studentsList.insert(0, 'Logan Ingram')
    writeListToFile(studentsList, 'names.txt')
    readList = readListFromFile('names.txt')
    print(readList)
    studentTuple = tuple(studentsList)


main()