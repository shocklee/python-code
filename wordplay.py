def length_greater(word, length):
    """Returns True if a given word is greater than the specified length."""
    return(len(word) > length)

def avoids(word, letters):
    """Returns True if the given word doesn't contain one of the forbidden
    letters in it."""
    for letter in word:
        if letter in letters:
            return False
    return True

def has_no_e(word):
    """Returns True if the given word doesn't contain the letter 'e'"""
    #return not 'e' in word
    return avoids(word, 'e')

def uses_only(word, letters):
    """Returns True if the given word contains only the letters in the list."""
    for letter in word:
        if letter not in letters:
            return False
    return True

def uses_all(word, letters):
    """Returns True if the given word used all the letters in the list at
    least once."""
    """for letter in letters:
        if letter not in word:
            return False
    return True"""
    return uses_only(letters, word)

def is_abecedarian(word):
    """Returns True if the letters in the word appear in alphabetical order."""
    previousLetter = word[0]
    for letter in word:
        if letter < previousLetter:
            return False
        previousLetter = letter
    return True

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    """Returns True if the word is a palindrome."""
    if(len(word) <= 1):
        return True       #Not enough letters left, we are done
    else:
        # len(word) > 1   #More than one letter left, continue
        if(first(word) == last(word)):
            return is_palindrome(middle(word))
        else:
            return False    

def readFile(filename):
    fin = open(filename)
    TOTAL_WORD_COUNT = 0
    LENGTH_COUNT = 0
    NO_E_COUNT = 0
    FORBIDDEN_COUNT = 0
    USES_ONLY_COUNT = 0
    USES_ALL_COUNT = 0
    ABECEDARIAN_COUNT = 0
    PALINDROME_COUNT = 0
    for line in fin:
        word = line.strip()
        TOTAL_WORD_COUNT += 1
        if(length_greater(word, 20)):
            LENGTH_COUNT += 1
            #print word
        if(has_no_e(word)):
            NO_E_COUNT += 1
            #print word
        if(avoids(word, 'etaon')):
            FORBIDDEN_COUNT += 1
            #print word
        if(uses_only(word, 'acefhlo')):
            USES_ONLY_COUNT += 1
            #print word
        if(uses_all(word, 'aeiou')):
            USES_ALL_COUNT += 1
            #print word
        if(is_abecedarian(word)):
            ABECEDARIAN_COUNT += 1
            #print word
        if(is_palindrome(word)):
            PALINDROME_COUNT += 1
            #print word
    fin.close()
    print 'Total word count:                  ', TOTAL_WORD_COUNT
    print 'Words greater than length:         ', LENGTH_COUNT
    print 'Words without e :                  ', NO_E_COUNT
    print 'Words without forbidden letters:   ', FORBIDDEN_COUNT
    print 'Words using only specific letters: ', USES_ONLY_COUNT
    print 'Words using all specific letters:  ', USES_ALL_COUNT
    print 'Words with sequencial letters:     ', ABECEDARIAN_COUNT
    print 'Palindrome count:                  ', PALINDROME_COUNT

readFile(r"C:\Users\shockma\Documents\Special\Python\words.txt")

