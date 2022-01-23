# Task 1
# Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.
# Hint: The string module provides strings named whitespace, which contains space, tab, newline, etc., punctuation which contains the punctuation characters and printable which contains printable characters.
# >>> import string
# >>> print (string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# Also, you might consider using the string methods strip and replace

from string import punctuation, whitespace

orange = 'apple'
Book1 = '%s.txt' % orange

with open(Book1, 'r') as fd:
    words = fd.read().split()

# removes punctuation white space and upper case letters
def clean(Words):
    cleansed = ''
    for char in Words:
        if (char in punctuation) or (char in whitespace):
            pass
        else:
            cleansed += char.lower()
    return cleansed


print()
"{} has {} 'words'".format(Book1, len([clean(word) for word in words]))
