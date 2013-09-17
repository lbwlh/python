my_list = [i**2 for i in range(1,11)]

#open
my_file = open("output.txt", "r+")

# Add your code below!
for item in my_list:
    my_file.write(str(item) + "\n")   #write
    
my_file.close()    #close

#read
print my_file.read()


#The 'with' and 'as' Keywords
with open("text.txt", "w") as my_file:
    my_file.write("Anything I want.")
    
if my_file.closed == False:
    my_file.close()
else:
    pass

print my_file.closed
