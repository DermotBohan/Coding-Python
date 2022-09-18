
##f = open ('10_01_file.txt', 'r')
##for line in f.readlines():
##    print(line.strip())
    


    #print(f)
    #f.readline()
    #f.readlines()

    
##f = open ('10_01_output.txt', 'w')
### print(f)    
##
##f.write('line 1\n')
##f.write('line 2\n')
##
##f.close()


# APPEND EXAMPLE
##f = open ('10_01_output.txt','a')
##f.write('line 3\n')
##f.write('line 4\n')
##f.close()

# CLOSE EXAMPLE / WITH STATEMENT
with open ('10_01_output.txt','a') as f:
    f.write('some stuff\n')
    f.write('some other stuff \n')
    
