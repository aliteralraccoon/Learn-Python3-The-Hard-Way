#Imports argv from sys
from sys import argv
#declares arguments
script, filename = argv
#opens the filename (specifices txt file)
txt = open(filename)
#
print(f"Here's your file {filename}:")
print(txt.read())
close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
close()
