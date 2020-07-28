#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    # Make own character set and pas
    # this as argument in compile method
    regex = re.compile('[@._!#$%^&*()<>?/\|}{~:]')
    # Pass the string in s 
    # method of regex object.
    if(regex.search(username) == 0):
        return True
    else:
        return False
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True
print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False


