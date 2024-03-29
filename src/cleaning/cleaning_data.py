import re
from typing import Callable

def has_character(string: str, character: str) -> int:
    """ A check to see if the 'character' is in the 'string'.
    
    :param string: The string to check.
    :param character: The character to match.

    :return: 1 if the character is found, 0 otherwise.

    >>> has_character("Aegon Targaryen (son of Rhaegar)", "(")
    1
    """

    if string == '': return 0
    if character in string: return 1
    else: return 0


def remove_pattern(string:str, pattern: str) -> str:
    """Removes the given pattern from the given string.

    Using regex to find a pattern and returning a string without the pattern.

    :param string: string to remove pattern from
    :paran pattern: a regex expression to match
    
    :return: string without pattern

    >>> remove_pattern("Aegon Targaryen (son of Rhaegar)", r".*?(\s\(.*?\))")
    "Aegon Targaryen"
    """

    # Compiling the regex pattern
    regex = re.compile(pattern)
    
    # This needs a try except block because if no matches are found slicing doesnt work
    try:
        result = re.findall(regex, string)[0]
    except IndexError:
        result = ''
    
    # Removing the match
    string = string.replace(result, '')
    return string

def count_words(string: str) -> int:
    """Counts how many words are in a string.

    :param string: String to count words in.

    :return: number of words

    >>> count_words("abc def ghi")
    3    
    """

    word_list = string.split(' ')

    try:
        word_list.remove('')
    except ValueError:
        pass
    
    count = len(word_list)

    return count

def generate_list(function: Callable, series: list, *args, **kwargs)-> list:
    """ Generates a list based on an input function.

    Uses a list comprehension to generate a list.

    :param function: function to use in the creation of the list
    :param series: List or series to iterate over to generate the list.
    :param *args: Any extra arguments that the input 'function' requires.
    :param **kwargs: Any key-word arguments the input 'function' requires.

    :return: list of values generated by the function.

    >>> generate_list(count_words, ["abc def", "ghi"])
    [2, 1]
    """

    # Generates a list with the outputs of `function` given the `string` in the `series`
    return [function(string, *args, **kwargs) for string in series]

def classify_domain(email: str, domain_type: str) -> int:
    """ Classifies whether an email is a given domain type.

    Given a list of which domains represent professional, personal, and junk domains, classify the email given as input

    :param email: The email to be classified
    :param domain_type: The domain type (professional, personal, or junk) to check

    :return: 1 if the specified domain type, 0 if not.

    >>> classify_domain("aegon.v.targaryen@goldmansacs.com", "professional")
    1
    """
    # Setting up a domain dictionary
    domain_dict = {"professional": ['mmm.com', 'amex.com', 'apple.com', 'boeing.com',
                                    'caterpillar.com', 'chevron.com', 'cisco.com', 'cocacola.com',
                                    'disney.com', 'dupont.com', 'exxon.com', 'ge.org',
                                    'goldmansacs.com', 'homedepot.com', 'ibm.com', 'intel.com',
                                    'jnj.com', 'jpmorgan.com', 'mcdonalds.com', 'merck.com',
                                    'microsoft.com', 'nike.com', 'pfizer.com', 'pg.com',
                                    'travelers.com', 'unitedtech.com', 'unitedhealth.com',
                                    'verizon.com', 'visa.com', 'walmart.com'],
                    
                    "personal":     ['gmail.com', 'yahoo.com', 'protonmail.com'],
                    
                    "junk":         ['me.com', 'aol.com', 'hotmail.com', 'live.com', 'msn.com', 'passport.com']}

    # Taking only the domain from the email
    domain = email.split('@')[1]

    if domain in domain_dict[domain_type]:  return 1
    else:                                   return 0

