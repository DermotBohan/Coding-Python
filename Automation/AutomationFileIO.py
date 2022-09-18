##f = open('inputFile.txt','r')
##count = 0
##for line in f:
##    print(str(count) + line)
##    count = count + 1
##  
##f.close()


## SPLIT FILE CONTENTS EXAMPLE
##f = open('ínputFile.txt','r')
##for line in f:
##    line_split = line.split()
##    if line_split[2] == 'P':
##        print(line)
##
##f.close()

# WRITE FILES EXAMPLE
##f = open('inputFile.txt','r')
##passFile = open('PassFile.txt','w')
##for line in f:
##    line_split = line.split()
##    if line_split[2] == 'P':
##        passFile.write(line)
##
##f.close()
##passFile.close()


## WRITE PASS SCORES TO FILE
f = open('inputFile.txt','r')
failFile = open('FailFile.txt','w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'F':
        failFile.write(line)

f.close()
failFile.close()
