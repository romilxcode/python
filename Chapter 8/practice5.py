# Print how many lines are present in notes.txt
import os

try:
    with open ("Chapter 8/notes.txt", "r") as f:
        listOfLines= f.readlines()
        print("Output of readLines Function", listOfLines)
        print("Number of Lines in File", len(listOfLines))

except:
    print("That File does not exist")
    
# RENAMING THE FILE

# os.rename("Chapter 8/reports2.txt", "Khushi.txt")
os.remove("Khushi.txt")
