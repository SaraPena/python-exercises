def keep_long_words():

    """
    >>> keep_long_words(['ls', 'codeup', 'code', 'pip', 'bayes'])
['codeup', 'bayes']
>>> keep_long_words(['cd', 'ls', 'pwd'])
[]
>>> keep_long_words(['python', 'algorithm'])
['python', 'algorithm']
"""
    long_words = []
    for word in words:
        if len(words) > 4:
            long_words.append(word)
    return long_words


    #loop through the words list
    #check that each word is longer than 4 characters.
    #return the list of long words

str({'make': 'Toyota', 'model': 'Camry'})




