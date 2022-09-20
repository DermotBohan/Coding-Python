# The Goal is to remove the duplicate sentences from the test string.
testString01 = "So, go ahead - Go ahead and explain to me the problem again? and explain to me the problem again."

testString02 = "So, go ahead - Go ahead and explain to me the problem again? and explain to me the problem again. - The interface on my tri-quarter - So the interface on my tricorder is not detecting life forms. is not detecting life forms. - Oh God, why do these Plutonians always have problems - Oh God, why do these Plutonians always have problems with tricorder, with tri-quarter, especially with life form readings? especially with life form readings? I mean, there's just something about them I mean, there's just something about them. and that's another problem I need to be careful about. And that's another problem I need to be careful about. You do not want to be judgmental towards your customer. You do not want to be judgemental towards your customer. Now, for you, this is a big deal, okay? Now, for you, this is a big deal, okay? Now for me, I probably already know Now, for me, I probably already know that there's a problem with your dilithium crystals there's a problem with your dilithium crystals in your tricorder that need to be adjusted, in your tri-quarter that need to be adjusted. But, the bottom line is, but the bottom line is, I don't want to be judgemental, I don't want to be judgmental and more importantly, and, more importantly, I don't want to dismiss these problems. I don't want to dismiss these problems. I can probably fix your tri-quarter in seconds, I can probably fix your tricorder in seconds, so it's easy for me to not really think about so it's easy for me to not really think what your problem is but more so, me, about what your problem is, but more so, me,"


# PSEUDO CODE
# Split the string into a list with split()
testList01 = testString01.split()
maxListIndex = len(testList01) - 1
# print(maxListIndex) # last index of list
counter = 0
for word in testList01:

    print(word)
    print(word.isalnum())
