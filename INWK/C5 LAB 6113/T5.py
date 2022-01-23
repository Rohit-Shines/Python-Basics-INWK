# Task 5
# Write a function called ‘sed’ that takes as arguments: two filenames;
# it should read the first file and write the contents into the second file (creating it if necessary).
# If an error occurs while opening, reading, writing, or closing files, your program should catch the exception, print an error message, and exit.

from __future__ import print_function, division

def sed(pattern, replace, source, dest):
    fin = open(source, 'r')
    fout = open(dest, 'w')

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)

    fin.close()
    fout.close()


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'orange.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main()