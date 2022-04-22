# Question 1:
# The “rank” of a word is its position in a list of words sorted by frequency: the most common word has rank 1, the second most common has rank 2, etc.
# Zipf’s law describes a relationship between the ranks and frequencies of words in natural languages (http://en.wikipedia.org/wiki/Zipf's_law). Specifically, it predicts that the frequency, f, of the word with rank r is:
# f = c* r **(-s)
# where s and c are parameters that depend on the language and the text. If you take the logarithm of both sides of this equation, you get:
# log f = log c − s log r
# So if you plot log f versus log r, you should get a straight line with slope −s and intercept log c.
# Write a program that reads a text from a file, counts word frequencies, and prints one line for each word, in descending order of frequency, with log f and log r. Use the graphing program of your choice to plot the results and check whether they form a straight line. Can you estimate the value of s?
# To make the plots, you might have to install matplotlib
# To plot using matplotlib:
# import matplotlib.pyplot as pyplot
# pyplot.clf()
# pyplot.xscale(scale)
# pyplot.yscale(scale)
# pyplot.title(“title string)
# pyplot.xlabel(“label string”)
# pyplot.ylabel(“label, string”)
# pyplot.plot(x-value, y-value)
# pyplot.show()
from operator import itemgetter  # importing operator
import pandas as pd  # importing pandas
from matplotlib import pyplot as plt  # to create the graph

frequency = {}  # creating a blank dictionary
file = open("Mango.txt", "r")  # opening the text file in read mode
words_doc = file.read()  # assigning contents of the file
splitted_words_doc = words_doc.split()

# calculate frequncy
for word in splitted_words_doc:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

rank = 1
column_header = ['Rank', 'Frequency', 'Frequency * Rank']
df = pd.DataFrame(columns=column_header)
collection = sorted(frequency.items(), key=itemgetter(1), reverse=True)

# To create a table of frequency * rank

for word, freq in collection:
    df.loc[word] = [rank, freq, rank * freq]
    rank = rank + 1

print(df)

# graphical representation of Frequency vs Words
plt.figure(figsize=(10, 10))
plt.ylabel("Frequency")
plt.xlabel("Words")
plt.xticks(rotation=90)

for word, freq in collection[:30]:
    plt.bar(word, freq)
plt.show()
