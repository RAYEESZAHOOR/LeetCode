# Given a positive integer n. You have to find nth natural number after removing all the numbers containing the digit 9.

class Solution:
    def findNth(self, n):
        # Convert n to a base-9 equivalent string, then convert it back to an integer
        res = ""
        while n > 0:
            res = str(n % 9) + res
            n //= 9
        return int(res)
