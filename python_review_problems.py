def keep_long_words(words):

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
        if len(word) > 4:
            long_words.append(word)
    return long_words


    #loop through the words list
    #check that each word is longer than 4 characters.
    #return the list of long words

def make_model(list_cars):
    """
    >>> cars = []
    >>> cars.append({'make': 'Toyota', 'model': 'Camry'})
    >>> cars.append({'make': 'Honda', 'model': 'Accord'})
    >>> cars.append({'make': 'Ford', 'model': 'Fiesta'})
    >>> cars.append({'make': 'Ford', 'model': 'F-150'})
    >>> make_model(cars)
    ['Toyota Camry', 'Honda Accord', 'Ford Fiesta', 'Ford F-150']
    """
    cars = []
    for car in list_cars:
        cars.append(car['make'] + ' ' + car['model'])
    return cars

def extract_time_components(s):
    """
    >>> extract_time_components('21:30:00')
    {'hours': 21, 'minutes': 30, 'seconds': 0}
    >>> extract_time_components('09:01:53')
    {'hours': 9, 'minutes': 1, 'seconds': 53}
    """
    etc = {}
    for times in s:
        etc['hours'] = int(s[0:2])
        etc['minutes'] = int(s[3:5])
        etc['seconds'] = int(s[6:])
    return etc

extract_time_components('09:01:53')




