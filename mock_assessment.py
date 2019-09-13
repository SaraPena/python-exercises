# 1. Define a function named ``normalize_name``. It should accept a string and
#    return a valid python identifier, that is:

#     - anything that is not a valid python identifier should be removed
#     - leading and trailing whitespace should be removed
#     - everything should be lowercase
#     - spaces should be replaced with underscores
#     - for example:
#         - ``Name`` will become ``name``
#         - ``First Name  `` will become ``first_name``
#         - ``% Completed`` will become ``completed``

#     >>> normalize_name('Name')
#     'name'
#     >>> normalize_name('First Name  ')
#     'first_name'
#     >>> normalize_name('% Completed')
#     'completed'

def normalize_name(s):
    for c in  ['%', '@', '$']:
        s = s.replace(c,"")
    return s.strip().lower().replace(" ","_")


# 2. Write a function named ``cumsum`` that accepts a list of numbers and returns
#    a list that is the cumulative sum of the numbers in the list.

#     - ``cumsum([1, 1, 1])`` returns ``[1, 2, 3]``
#     - ``cumsum([1, 2, 3, 4])`` returns ``[1, 3, 6, 10]``

#     >>> cumsum([1, 1, 1])
#     [1, 2, 3]
#     >>> cumsum([1, 2, 3, 4])
#     [1, 3, 6, 10]

def cumsum(x):
    answer = list() 
    count = 0
    for number in x:
        answer.append(number+count)
        count += number
    return answer

cumsum([1,1,1])



