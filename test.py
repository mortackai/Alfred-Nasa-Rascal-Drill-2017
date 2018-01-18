pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
else:
    print 'empty'
    
new_word = word + first + pyg
print new_word[1:len(new_word)]
