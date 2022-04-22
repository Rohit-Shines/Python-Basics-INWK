# Q2
# In a large collection of MP3 files, there may be more than one copy of the same song, stored in different
# directories or with different file names. The goal of this exercise is to search for duplicates.
# 1. Write a program that searches a directory and all of its subdirectories, recursively, and returns a
# list  of  complete  paths  for  all  files  with  a  given  suffix  (like  .mp3).  Hint:  os.path  provides  several
# useful functions for manipulating file and path names.
# 2. To recognize duplicates, you can use md5sum to compute a “checksum” for each files. If two files
# have the same checksum, they probably have the same contents.
# 3. To double-check, you can use the Unix command diff.




# Importing Libraries
import os
from pathlib import Path
from filecmp import cmp


# list of all documents
DATA_DIR = Path('/Users/rohitkumargundu/Downloads/Leet Code All Solutions')
files = sorted(os.listdir(DATA_DIR))

# List having the classes of documents
# with the same content
duplicateFiles = []

# comparison of the documents
for file_x in files:

	if_dupl = False

	for class_ in duplicateFiles:
		# Comparing files having same content using cmp()
		# class_[0] represents a class having same content
		if_dupl = cmp(
			DATA_DIR / file_x,
			DATA_DIR / class_[0],
			shallow=False
		)
		if if_dupl:
			class_.append(file_x)
			break

	if not if_dupl:
		duplicateFiles.append([file_x])

# Print results
print(duplicateFiles)
