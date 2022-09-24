secret = "swordfish"
pw = ""

auth = False
count = 0
maxAttempt = 5

while pw != secret:
    count += 1
    if count > maxAttempt:
        break
    if count == 3:
        continue
    pw = input(f"{count}: What is the secrret word?")
else:
    auth = True

print("Authorized" if auth else "I'm calling the FBI!")
