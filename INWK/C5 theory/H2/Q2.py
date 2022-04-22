# Question 2:
# Write a function called ‘sed’ that takes as arguments: two filenames.
# it should read the first file and write the contents into the second file (creating it if necessary).
# If an error occurs while opening, reading, writing, or closing files, your program should catch the exception, print an error message, and exit.
# Question 3 (Bonus for your Self Appreciation):
# In a large collection of MP3 files, there may be more than one copy of the same song, stored in different directories or with different file names. The goal of this exercise is to search for duplicates.
# 1. Write a program that searches a directory and all of its subdirectories, recursively, and returns a list of complete paths for all files with a given suffix (like .mp3). Hint: os.path provides several useful functions for manipulating file and path names.
# 2. To recognize duplicates, you can use md5sum to compute a “checksum” for each files. If two files have the same checksum, they probably have the same contents.
# 3. To double-check, you can use the Unix command diff.

def sed(file_1,file_2):
  with open(file_1,"r") as f:
    with open(file_2, "w") as f1:
        for line in f:
            f1.write(line)
  print("The contents of File 1 has been copied to File 2")

sed("Mango.txt","Mango.txt")

