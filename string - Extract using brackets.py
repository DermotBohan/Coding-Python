str1 = "Cisco IOSv Router."
print(str1)                 # Cisco IOSv Router.
print(str1[0])              # C
print(str1[-3])             # e in router
print(len(str1))  # 18
print(str1[0].isalnum())    # True
print(str1[-1].isalnum())   # False
print(str1[len(str1) - 1])  # last character
print(str1[len(str1) - 2])  # second last character
print(str1[0:len(str1) - 1])  # All characters minus the last character
print(str1[0:17])           # Cisco IOSv Router
