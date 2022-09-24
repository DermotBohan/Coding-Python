# pyperclip so strings can be copied to the clipboard for testing purposes.
import pyperclip
import string

# The Goal is to remove the duplicate sentences from the test string.
# Duplicate words are written sometimes with capital letters so reduce all case to lower for better chance at matches.
# some duplicated words have only single instances of non alpha numeric characters (?.etc) at the end which will need to be rectified.

# pyperclip.copy(testStringLower)


# Split the string into a list with split()
# Use the list to chain words together and count() to track matches
# go past a certain number of matches before examination - 3 as a starting point
# NOTE Python comparison operators are usual: == != < > <= >=
# NOTE print(string.punctuation)
# x = "/"
# print(x in string.punctuation)
print(string.punctuation)


def buildStringChain(listIndex, accumulator):
    stringChain = testList[listIndex]
    print(f'stringChain test: {stringChain}')
    i = 0
    while (i < accumulator):
        stringChain += " "+testList[listIndex + 1 + i]
        print(f'stringChain addition test: {stringChain}')
        i += 1
    return stringChain


def performTest(testString, stringChain):
    result = testString.count(stringChain)
    return result


def reportFindings(testList, stringChain, result, listIndex, accumulator):
    print('REPORTING FINDINGS:')
    print(f'testList: {testList}')
    print(f'stringChain: {stringChain}')
    print(f'result: {result}')
    print(f'listIndex: {listIndex}')
    print(f'accumulator: {accumulator}')


# reportFindings(testList, stringChain, result)


def parseContent(listIndex, accumulator, testList):
    stringChain = buildStringChain(listIndex, accumulator)
    result = performTest(testString, stringChain)
    # reportFindings(testList, stringChain, result, listIndex, accumulator)

    # No other matches for this item, no duplicate strings exist containing this item.
    if result == 1:
        # If accumulator is 0 then Move to next item
        reportFindings(testList, stringChain, result, listIndex, accumulator)
        # print("No match found. Moving ListIndex onto next word and restarting test for duplicates.")

        if accumulator == 0:
            print('No match found and no build up of stringChain either.')
            print(
                'Moving ListIndex onto next word, resetting accumulator, and restarting test for duplicates.')
            # start again, stringChain beginning with the next word along in the sequence.
            listIndex += 1
            accumulator = 0
            parseContent(listIndex, accumulator, testList)
        else:
            print(
                "No match found, but as stringChain exists, further investigation of stringChain needed")

            # IS there something wrong up with the last word?

            # TEST 02
            if testList[listIndex] == testList[listIndex + accumulator]:
                print(
                    f'LAST WORD: {testList[listIndex + accumulator]} matches FIRST WORD: {testList[listIndex]}')
                if accumulator < 4:
                    print(
                        f'length of stringChain has not passed the set level to warrant deletion.')
                    print(
                        'Moving ListIndex onto next word, resetting accumulator, and restarting test for duplicates.')
                    listIndex += 1
                    accumulator = 0
                    parseContent(listIndex, accumulator, testList)
                else:
                    print(
                        'Time to update testString and then remove the duplicate words from testList')
                    del testList[listIndex:(listIndex + accumulator)]
                    print('Duplicate sentence removed from testList.')
                    print(f'testList present state: {testList}')
                    # resetCounters
                    listIndex = 0
                    accumulator = 0
                    print('PROCESS HALTED!!!!')
            else:
                print(
                    f'LAST WORD: {testList[listIndex + accumulator]} DOES NOT match FIRST WORD: {testList[listIndex]}')
                print('So no loop has been identified.')
                print(
                    'This has occured because the first word in the stringChain matched with a previous word in the list.')
                print(
                    'Continuing for now but this is possibly a bug. The line that caused it: choo choo cholly')
                print(
                    'Moving ListIndex onto next word, resetting accumulator, and restarting test for duplicates.')
                listIndex += 1
                accumulator = 0
                parseContent(listIndex, accumulator, testList)
            # If accumulator > 0 then dublicate chains have been detected. Further investigation is now needed.
            # listIndex = listIndex + 1                                     # starting word from list
            # multiplier = 1                                                # use for assembling stringChain
            # accumulator = 0                                               # How many words match successfully
            # Duplicate strings have been found.
    elif result > 1:

        reportFindings(testList, stringChain, result, listIndex, accumulator)
        print('Match Found')
        print('increasing accumulator and continuing with PARSING')
        accumulator += 1
        # Add the next item to the stringChain and check again for duplicate string
        parseContent(listIndex, accumulator, testList)

    else:
        print('Error encountered with code.')


# inputString = "So, go ahead - Go ahead and explain to me the problem again? and explain to me the problem again."
# inputString = "go ahead - Go ahead and explain to me the problem again? and explain to me the problem again."
# inputString = "choo choo cholly, no sense of time. This is a test this is a test"
# inputString = "This is. a test this- is a test"
inputString = "now This is a test this is a test"
testString = inputString.lower()
# I think here we should check for punctuation or numbers and add a space before and after any occurances.
# This will need to be accounted for when removing/updating the testList

testList = testString.split()
listIndex = 0
accumulator = 0
parseContent(listIndex, accumulator, testList)

# del game[3]
punctuation = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-',
               '.', '/', ':', ';', '<', '=', '>', '?', '@', '^', '_', '|', '~']
subTestList = ["dumb", "5titch", "$ededed"]

# for x in subTestList:
#     print(f'X: {x}')
#     if x.isalpha():
#         print(f'Pass for: {x}')
#     else:
#         wordLength = len(x)
#         print(f'wordLength: {wordLength}')
#         i = 0
#         while i < wordLength:
#             if x[i].isnumeric():
#                 print('Word contains a Numeric character.')
#             if x[i] in punctuation:
#                 print('wird contains a punctuation character.')
#             i += 1
#         print('done')


# print(type(testList))


# print("test5".isalpha())
# print("test5".isnumeric())


# print(len("test5"))
# word = "banana"
# print(word[0])
# print(word)
# word = word.replace(word[1], '', 1)
# print(word)


# print(result)

# Required numbers????
# maxListIndex = len(testList) - 1
# print(maxListIndex) # last index of list
# counter = 0
# for word in testList01:
#     print(word)
#     print(word.isalnum())


# 01) Remove all non alpha characters


# str2 = str1.split()
# print(str1.count(str2[0]+" "+str2[1]))
# print(str1.count(str2[1]))
