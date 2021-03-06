"""The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of lists containing two items each. Each list contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

Note for F#: The input will be of (int list list) which is a List>

Example Input
[[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
Output
Output will consist of a list of string values (in Haskell: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

Example Output
["Open", "Open", "Senior", "Open", "Open", "Senior"]"""


def openOrSenior(data):
    return ["Senior" if age >= 55 and hand > 7 else "Open" for (age, hand) in data]


#List comprehension arrays

l3 = [x for x in l1 if x not in l2]

"""Capitalize the first letter of each word"""


import string     # Works better than .title, doesn't cap after apostrophes.

def toJadenCase(NonJadenStrings):
    return string.capwords(NonJadenStrings)


#Simple, given a string of words, return the length of the shortest word(s).
#My solution:
def find_short(s):
    w = s.split(' ')
    sortedwords = sorted(w, key=len)
    selection = sortedwords[0]
    return len(selection)


#Best solution:

def find_short(s):
    return min(len(x) for x in s.split())


"""title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'"""

# def title_case(title, minor_words=''):
#     title = title.capitalize().split()
#     minor_words = minor_words.lower().split()
#     return ' '.join([word if word in minor_words else word.capitalize() for word in title])
