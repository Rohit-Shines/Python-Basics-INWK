# Task 2: Modify your program from the previous exercise to read the book you downloaded and process the rest of the
# words as before. A. Then modify the program to count the total number of words in the book, and the number of times
# each word is used. B. print the 20 most frequently-used words in the book. C. Print the number of different words
# used in the book Optional: write a function that takes in any number of books and produce the book with the
# greatest number of words

import string
import time

def del_punctuation(item):
    punctuation = string.punctuation
    for c in item:
        if c in punctuation:
            item = item.replace(c, '')
    return item

def break_into_words():
    textBook = open('lab0.txt')
    words_list = []
    for line in textBook:
        for item in line.split():
            item = del_punctuation(item)
            item = item.lower()
            # print(item)
            words_list.append(item)
    return words_list


def create_dict():
    words_list = break_into_words()
    dictionary = {}
    for word in words_list:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1

    return dictionary


dictionary = create_dict()
dictionary.pop('', None)
start_time = time.time()
print('The total number of words in the book is {}'.format(len(break_into_words())))
print('The number of different words used in the book {}'.format(len(dictionary)))
function_time = time.time() - start_time

print('Running time is {0:.4f} s'.format(function_time))

