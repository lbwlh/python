from sys import argv

#sc, f, s, t = argv

#print "The script is called:", sc
#print "Your first variable is:", f
#print "Your second variable is:", s
#print "Your third variable is:", t

#exercise with raw_input
script, user_name = argv
prompt = '>  '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
