# A string consists of parenthesis and letters. validate if all the parenthesis are balanced.
# all three type of parenthesis are possible - '()', '[]', '{}','<>'
# Solution:
# One approach to check balanced parentheses is to use stack.
# Each time, when an open parentheses is encountered push it in the stack,
# and when closed parenthesis is encountered, match it with the top of stack
# and pop it. If stack is empty at the end, return Balanced otherwise, Unbalanced.
