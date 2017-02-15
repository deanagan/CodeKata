#!/usr/bin/python


def checkio(expression):
    bracket_pairs = ('{}', '[]', '()')
    clean = "".join(i if i in ('{','(','[',']',')','}') else '' for i in expression)

    while any(str in clean for str in bracket_pairs):
        clean = clean.replace('()','').replace('[]', '').replace('{}','')

    return len(clean) == 0

#alt solution
def checkio(expression):
    bracket_pairs = {'{':'}', '[':']', '(':')'}

    stack = []
    for ch in expression:
        if ch in bracket_pairs:
            stack.append(ch)
        elif len(stack) > 0 and bracket_pairs[stack[-1]] == ch:
            stack.pop() 
        elif ch in bracket_pairs.values():
            return False

    return len(stack) == 0
