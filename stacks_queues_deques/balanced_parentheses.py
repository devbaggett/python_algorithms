# balanced_parentheses

# Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round
# brackets: (), square brackets: [], and curly brackets: {}. Assume that the string doesn’t contain any other character
# than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be
# closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not.

# You can assume the input string has no spaces.

from tests.tests import TestBalanceCheck
from CreateStack import Stack


def balanced_parentheses(string):
    if len(string) % 2 != 0:
        return False

    opening = set('([{')
    matches = {('(', ')'), ('[', ']'), ('{', '}')}
    stack = Stack()
    for parentheses in string:
        if parentheses in opening:
            stack.push(parentheses)
        else:
            if stack.size() == 0:
                return False

            last_open = stack.pop()
            if (last_open, parentheses) not in matches:
                return False

    return stack.size() == 0


t = TestBalanceCheck()
t.test(balanced_parentheses)
