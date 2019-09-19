def isnegative(x):
    """
    >>> from solutions import isnegative
    >>> type(isnegative(0))
    <class 'bool'>
    >>> isnegative(4)
    False
    >>> isnegative(0)
    False
    >>> isnegative(-6)
    True
    """
    if x < 0 :
        return True
    return False

assert type(isnegative(0)) == bool
assert isnegative(4) == False
assert isnegative(0) == False
assert isnegative(-6) == True

def count_evens(l):
    """
    >>> from solutions import count_evens
    >>> type(count_evens([1, 2, 3]))
    <class 'int'>
    >>> count_evens([1, 2, 3])
    1
    >>> count_evens([4, 6, 8, 10, 12])
    5
    >>> count_evens([1, 3, 5, 7, 9])
    0
    >>> count_evens([])
    0
    >>> count_evens([3, 2])
    1
    """
    evens = []
    c = 0
    for number in l:
        if number % 2 == 0:
            c += 1
    return c

assert type(count_evens([1, 2, 3])) == int
assert count_evens([1, 2, 3]) == 1
assert count_evens([4, 6, 8, 10, 12]) == 5
assert count_evens([1, 3, 5, 7, 9]) == 0
assert count_evens([]) == 0
assert count_evens([3, 2]) == 1

def increment_odds(l):
    """
    >>> from solutions import increment_odds
    >>> type(increment_odds([1, 2, 3]))
    <class 'list'>
    >>> increment_odds([1, 2, 3])
    [2, 2, 4]
    >>> increment_odds([2, 2, 1, 4, 5])
    [2, 2, 2, 4, 6]
    >>> increment_odds([])
    []
    >>> increment_odds([0, 1])
    [0, 2]
    """
    odd_increment = []
    for number in l:
        if number % 2 == 1:
            number += 1
            odd_increment.append(number)
        else:
            odd_increment.append(number)
    return odd_increment

assert type(increment_odds([1, 2, 3])) == list
assert increment_odds([1, 2, 3]) == [2, 2, 4]
assert increment_odds([2, 2, 1, 4, 5]) == [2, 2, 2, 4, 6]
assert increment_odds([]) == []
assert increment_odds([0, 1]) == [0, 2]

def average(l):
    """
    >>> from solutions import average
    >>> type(average([1, 2, 3]))
    <class 'float'>
    >>> average([1, 2, 3])
    2.0
    >>> average([4, 6, 8, 10, 12])
    8.0
    >>> average([1, 2])
    1.5
    """
    return float(sum(l)/len(l))


assert type(average([1, 2, 3])) == float
assert average([1, 2, 3]) == 2.0
assert average([4, 6, 8, 10, 12]) == 8.0
assert average([1, 2]) == 1.5

def name_to_dict(s):
    """
    >>> from solutions import name_to_dict
    >>> type(name_to_dict('Ada Lovelace'))
    <class 'dict'>
    >>> name_to_dict('Ada Lovelace')
    {'first_name': 'Ada', 'last_name': 'Lovelace'}
    >>> name_to_dict('Marie Curie')
    {'first_name': 'Marie', 'last_name': 'Curie'}
    """
    n = {}
    s = s.split()
    n['first_name'] = s[0]
    n['last_name'] = s[1]
    return n

assert type(name_to_dict('Ada Lovelace')) == dict
assert name_to_dict('Ada Lovelace') == {'first_name': 'Ada', 'last_name': 'Lovelace'}
assert name_to_dict('Marie Curie') == {'first_name': 'Marie', 'last_name': 'Curie'}


def capitalize_names(l):
    """
    >>> from solutions import capitalize_names
    >>> names = []
    >>> names.append({'first_name': 'ada', 'last_name': 'lovelace'})
    >>> names.append({'first_name': 'marie', 'last_name': 'curie'})
    >>> names
    [{'first_name': 'ada', 'last_name': 'lovelace'}, {'first_name': 'marie', 'last_name': 'curie'}]
    >>> type(names)
    <class 'list'>
    >>> capitalize_names(names)
    [{'first_name': 'Ada', 'last_name': 'Lovelace'}, {'first_name': 'Marie', 'last_name': 'Curie'}]
    >>> type(capitalize_names(names))
    <class 'list'>
    """
    names = []
    for dictionary in l:
        dictionary['first_name'] = dictionary['first_name'].capitalize()
        dictionary['last_name'] = dictionary['last_name'].capitalize()
        names.append(dictionary)
    return names

names = []
names.append({'first_name': 'ada', 'last_name': 'lovelace'})
names.append({'first_name': 'marie', 'last_name': 'curie'})
names
type(names) == list

    
assert type(names) == list
assert capitalize_names(names) == [{'first_name': 'Ada', 'last_name': 'Lovelace'}, {'first_name': 'Marie', 'last_name': 'Curie'}]
assert type(capitalize_names(names)) == list

def count_vowels(s):
    """
    >>> from solutions import count_vowels
    >>> type(count_vowels('codeup'))
    <class 'int'>
    >>> count_vowels('codeup')
    3
    >>> count_vowels('abcde')
    2
    >>> count_vowels('why')
    0
    """
    vowels = ['a','e','i','o','u']
    c = 0
    for character in s:
        if character in vowels:
            c +=1
    return c

assert type(count_vowels('codeup')) == int
assert count_vowels('codeup') == 3
assert count_vowels('abcde') == 2
assert count_vowels('why') == 0

def analyze_word(s):
    """
    >>> from solutions import analyze_word
    >>> type(analyze_word('codeup'))
    <class 'dict'>
    >>> analyze_word('codeup')
    {'word': 'codeup', 'n_letters': 6, 'n_vowels': 3}
    >>> analyze_word('abcde')
    {'word': 'abcde', 'n_letters': 5, 'n_vowels': 2}
    >>> analyze_word('why')
    {'word': 'why', 'n_letters': 3, 'n_vowels': 0}
    """

    a = {}
    a['word'] = s
    a['n_letters'] = len(s)
    a['n_vowels'] = count_vowels(s)
    
    return a


assert type(analyze_word('codeup')) == dict
assert analyze_word('codeup') == {'word': 'codeup', 'n_letters': 6, 'n_vowels': 3}
assert analyze_word('abcde') == {'word': 'abcde', 'n_letters': 5, 'n_vowels': 2}
assert analyze_word('why') ==  {'word': 'why', 'n_letters': 3, 'n_vowels': 0}