
# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

# The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Memoization to store results of sub-expressions
        memo = {}

        # Helper function to compute the result recursively
        def compute(expr):
            # If the expression has already been computed, return the cached result
            if expr in memo:
                return memo[expr]
            
            # Result list for this sub-expression
            res = []
            
            # Iterate through the expression
            for i in range(len(expr)):
                if expr[i] in '+-*':  # If the character is an operator
                    # Split the expression into two parts and recursively compute their results
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    
                    # Apply the operator to every combination of results from left and right parts
                    for l in left:
                        for r in right:
                            if expr[i] == '+':
                                res.append(l + r)
                            elif expr[i] == '-':
                                res.append(l - r)
                            elif expr[i] == '*':
                                res.append(l * r)
            
            # If no operator is found, it means the expression is a single number
            if not res:
                res.append(int(expr))
            
            # Cache the result for this sub-expression
            memo[expr] = res
            return res
        
        # Call the helper function on the full expression
        return compute(expression)