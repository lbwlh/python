pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
        new_word = word + pyg
        print "Translate to PygLatin word : %s" % new_word
    else:
        new_word = word[1:len(word)] + first + pyg
        print "Translate to PygLatin word : %s" % new_word
else:
    print 'empty'
