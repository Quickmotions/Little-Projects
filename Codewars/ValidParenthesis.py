# FERGUS HAAK 26/07/21
# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python
# work in progress
def valid_parentheses(string):
    open_list = 0
    closed_list = 0
    bracket = ''
    for val in range(len(string)):
        if string[val] == '(':
            bracket += '('
            open_list += 1
        if string[val] == ')':
            closed_list += 1
            bracket += ')'
    if bracket == '':
        return True
    if closed_list == open_list and bracket[-1] == ')' and bracket[0] == '(':
        return True
    else:
        return False

    # should test as it runs through to make sure it cant close 2 brackets when only 1 is open ect...