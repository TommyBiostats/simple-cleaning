
dirty_list = ['bayern.12-05-2012', 'borucia dortmund.13-07.2023', 'anamanta di caltino .12-03;2019']

import re

def extract_symbols_entry(entry, symbols, joiner, exception):
    if symbols == 'characters':
        words = re.findall(fr'[^\W\d_]+|{exception}+', entry)
        result = joiner.join(words)
        result = result.lower()
        return result
    elif symbols == 'numbers':
        nums = re.findall(r'[0-9]+', entry)
        result = joiner.join(nums)
        return result
    else:
        print('Please enter either \'characters\' or \'numbers\' as symbols.')



def extract_relevant(list, symbols, joiner = '_', exception = None):

    '''
    This function extracts the information you consider relevant, and returns a 'clean' list. In symbols field you can choose either characters or numbers.
    Joiner is any sign that you would like to join the elements with - by default it is '_'. Optionally, you can choose an 'exception' sign, for instance,
    if you want to know if the entry was an email, you can enter '@' in the exception field, and '@' will remain present in the entries, even though it is not
    a character/number.
    '''

    if symbols in ['characters', 'numbers']:
        clean_list = []
        for entry in list:
            clean_entry = extract_symbols_entry(entry, symbols,joiner, exception)
            clean_list.append(clean_entry)
        return clean_list
    else:
        print('Please enter either \'characters\' or \'numbers\' as symbols.')

#I used ChatGpt to create some messy list to test the function
data = [
    "johndoe@123 ",        # Whitespace, inconsistent formatting
    "alice!!20$$",         # Special characters
    "tim30",               # No space between name and age
    "bob,28",              # Incorrect delimiter
    "susan##35%%",         # Special characters
    "Eve 22years",         # Inconsistent format ("years" word is unexpected)
    " john 29",            # Leading space
    "hannah !!!    31 ",   # Multiple unnecessary characters
    "johnny_27",           # Underscore instead of space
    "carol1980",           # Birth year, not age
    " 1985eric",           # Missing name and inconsistent format
    "  35, james    ##",    # Extra spaces, special characters
    "sarah_45 _active",    # Mixed info in one field (age and status)
    "mark#35??",           # Special characters
    " info:45, no-name",   # Inconsistent labeling
    ",,,jamie,,38,,",      # Excessive commas
    "david@#23extra",      # Special characters with extra text
]

print(extract_relevant.__doc__)

print(extract_relevant(list = dirty_list, symbols = 'numbers', joiner = '.'))


