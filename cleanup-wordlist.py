import os

#open file1 in reading mode (download from https://raw.githubusercontent.com/OpenTaal/opentaal-wordlist/master/elements/basiswoorden-gekeurd.txt)
file1 = open('basiswoorden-gekeurd.txt', 'r')

#open file2 in writing mode
file2 = open('js/wordlist.js','w')

# Write beginning of file
file2.write("var wordlist = [\n")

#read from file1 and write to file2
for line in file1:

    # Strip line
    strippedline = line.strip().lower()

    # Filter out small or large words
    if len(strippedline) < 4 or len(strippedline) > 8:
        continue

    # Check digits
    if any(char.isdigit() for char in strippedline):
        continue

    # Check spaces in word
    if (' ' in strippedline) == True:
        continue

    # Check alnum
    if strippedline.isalnum() == False:
        continue

    strippedline = " '"+strippedline+"',\n"

    file2.write(strippedline)

# Write end of file
file2.write("];")

#close file1 and file2
file1.close()
file2.close()
