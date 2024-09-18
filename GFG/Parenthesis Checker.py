# Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
# For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

# Note: The driver code prints "balanced" if function return true, otherwise it prints "not balanced".

#User function Template for python3

class Solution:
    
    def ispar(self, s):
        stack = []
        
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if stack and ((stack[-1] == '(' and char == ')') or
                              (stack[-1] == '{' and char == '}') or
                              (stack[-1] == '[' and char == ']')):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
