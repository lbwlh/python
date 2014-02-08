def make_list(ranges, steps):
	i = 0
	numbers = []

	while i < ranges:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + steps
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

prompt = '>  '

print "How long do you want the list to be?"
ranger = int(raw_input(prompt))

print "How long step do you want the list to be?"
step = int(raw_input(prompt))

make_list(ranger, step)
