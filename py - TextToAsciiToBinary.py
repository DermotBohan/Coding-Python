# Converts a letter first to its ascii equivalent
# then to binary, removing the b from the binary bin() output

import os


def addToClipBoard(text):
    command = "echo " + text.strip() + "| clip"
    os.system(command)


inputValue = input("enter value:")
asciiValue = ord(inputValue)
binaryValue = bin(asciiValue).replace('b', '')
# binaryValue = bin(asciiValue)

print(f"binary value of {inputValue}:", binaryValue)
addToClipBoard(binaryValue)
