"""
We are given strings containing brackets of 4 types - round (), square [], curly {} and angle <> ones. 
The goal is to check, whether brackets are in correct sequence. I.e. any opening bracket should 
have closing bracket of the same type somewhere further by the string, and bracket pairs should not overlap, 
though they could be nested.

"""

def checkBalance(string, pairs = {'[': ']', '{': '}', '(': ')', '<': '>'}):
    opening = list(pairs.keys())
    closing = list(pairs.values())
    match = list()
    for value in string:
        if value in opening:
            match.insert(0, value)
        elif value in closing:
            if len(match) == 0:
                return False
            if match[0] == opening[closing.index(value)]:
                match.pop(0)
            else:
                return False

    if len(match) == 0:
        return True
    return False

if __name__ == "__main__":
    result = checkBalance('{<ankit)>}')
    if result:
        print("String is balanced")
    else:
        print ("Try Again!!! string is Not balanced")
