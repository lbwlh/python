from sys import argv

my_list = [i**2 for i in range(1,11)]

#open
my_file = open("output.txt", "r+")

# Add your code below!
for item in my_list:
    my_file.write(str(item) + "\n")   #write

my_file = open("output.txt", "r+")
print my_file.read()

my_file.truncate()
   
#The 'with' and 'as' Keywords
with open("text.txt", "w") as my_file:
    my_file.write("Anything I want.")

if my_file.closed == False:
    my_file.close()
else:
    pass

print my_file.closed

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
