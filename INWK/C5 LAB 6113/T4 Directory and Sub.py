# Task 4
# The os module provides a function called walk that is similar to one below but more versatile.
# Read the documentation and use it to print the names of the files in a given directory and its subdirectories.


import os

'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def main():
    dirName = '/Users/rohitkumargundu/Downloads/Leet Code All Solutions';

    listOfFiles = getListOfFiles(dirName)

    for elem in listOfFiles:
        print(elem)
    print("****************")
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    # Print the files
    for elem in listOfFiles:
        print(elem)


if __name__ == '__main__':
    main()