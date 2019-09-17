'bayes' #string literal

my_string = 'bayes'
my_string

1 + 1

'1' + '1'

'a' * 10

##we can't always use every operator with every data type.

[] / {} #We cannot divide a list by a dictionary.

x = 3 # '=' means assign
x < 10

x > 0

# Comparison operators return boolean values.

'happy tuesday, bayes!'.upper()

# Suggestion: Know how you can research the function you need. i.e. how to use Google.

# Can convert between types.
x = 123
for digit in str(x):
    print(digit)

s = '456 test'
int(s) + 1

# String formatting
name = 'world'

'Hello, ' + name + '!'
"Hello, %s" % name
'Hello {}!'.format(name)
f'Hello {name}!'

my_list = [1, 2, 3, 4, 5]

my_list.append(6)
my_list

my_list.pop()

my_list.remove(2)
my_list

all_ones = [1, 1, 1, 1, 1]
all_ones.remove(1)
all_ones

my_list[0]
my_list[1:]

# List comprehension

[n for n in my_list]
[n+1 for n in my_list]

# Can put a boolean after 'if' in a list comprehension
[n+1 for n in my_list if n==3]

# Tuples
my_tuple = (1, 'one')
my_tuple[0]
my_tuple[1]

# dictionaries
{'name' : 'Zach', 'favorite_language' : 'python'}
me = {}
me['name'] = 'Zach'
me['favorite_language'] = 'python'
me

# reassign values in dictionaries

me['name'] = me['name'].lower()
me

# rename key

me ['capitalize_name'] = me['name'].capitalize()

# List of dictionaries

instructors = [{'name': 'Zach', 'favorite_language': 'clojure'},{'name' : 'David', 'favorite_language' : 'matlab'},{'name': 'Maggie', 'favorite_language': 'python'}]
type(instructors[0])

instructors[1]['favorite_language']

for instructor in instructors:
    print("{}'s favorite language is {}".format(instructor['name'], instructor['favorite_language']))

for instructor in instructors:
    if instructor['name'] != 'Zach':
        continue
    print('--------')
    print(instructor['name'])
    print(instructor['favorite_language'])

## Who likes matlab??

for instructor in instructors:
    if instructor['favorite_language'] == 'matlab':
        print('{} likes matlab!'.format(instructor['name']))

# WHo likes matlab? -- more broadly, who likes a given language?
# return the names of the instructors who like the language

def who_likes_language(instructors):
    instructors_that_like_the_language = []
    for instructor in instructors:
        if instructor['favorite_language'] == 'matlab':
            instructors_that_like_the_language.append(instructor['name'])
    return instructors_that_like_the_language

who_likes_language(instructors)

instructors2 = [{'name': 'Zach', 'favorite_language': 'clojure'},{'name' : 'David', 'favorite_language' : 'matlab'},{'name': 'Maggie', 'favorite_language': 'matlab'}]

who_likes_language(instructors2)

def who_likes_language(instructors):
    instructors_that_like_the_language = []
    for instructor in instructors:
        print('Debug: looking at instructor: {}'.format(instructor['name']))
        if instructor['favorite_language'] == 'matlab':
            print('Debug: adding {}'.format(instructor['name']))
            instructors_that_like_the_language.append(instructor['name'])
        else:
            print('Debug: not adding {}'.format(instructor['name']))
    return instructors_that_like_the_language

def who_likes_language(instructors,language):
    instructors_that_like_the_language = []
    for instructor in instructors:
        print('Debug: looking at instructor: {}'.format(instructor['name']))
        if instructor['favorite_language'] == language:
            print('Debug: adding {}'.format(instructor['name']))
            instructors_that_like_the_language.append(instructor['name'])
        else:
            print('Debug: not adding {}'.format(instructor['name']))
    return instructors_that_like_the_language

who_likes_language(instructors2,'matlab')