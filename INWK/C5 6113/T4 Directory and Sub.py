# Task 4
# The os module provides a function called walk that is similar to one below but more versatile.
# Read the documentation and use it to print the names of the files in a given directory and its subdirectories.


import os

'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def main():
    dirName = '/Users/rohitkumargundu/Downloads/Leet Code All Solutions';

    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)

    # Print the files
    for elem in listOfFiles:
        print(elem)
    print("****************")

    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    # Print the files
    for elem in listOfFiles:
        print(elem)


if __name__ == '__main__':
    main()