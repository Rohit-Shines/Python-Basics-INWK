import string
from bisect import bisect_left

def make_wordlist(file):
    result = []
    wordlist = open(file)
    for line in wordlist:
        word = line.strip()
        result += [word]
    return result

wordlist = make_wordlist("lab0.txt")


def in_bisect(word_list, word):
    i = bisect_left(word_list, word)
    return i != len(word_list) and word_list[i] == word


def find_words_not_in_wordlist(a_file, wordlist, start_line=1):
    new_text = []
    fin = open(a_file)
    lines = fin.readlines()
    lines = lines[start_line - 1:]
    punctuations = string.punctuation
    punctuations = punctuations.replace("-", "")

    for line in lines:
        stripped_line = line.strip().lower().replace("--", " ").translate(string.maketrans("", ""), punctuations).split()
        new_text += stripped_line

    word_count_dict = {}
    for word in new_text:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    not_in_wordlist = []
    for item in word_count_dict.keys():
        if not in_bisect(wordlist, item):
            not_in_wordlist += [item]
    return not_in_wordlist