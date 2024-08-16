# # Lemonade Change
# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

class Solution(object):
    def lemonadeChange(self, bills):
        if bills[0] != 5:
            return False
        
        five_dollers = 0
        ten_dollers = 0

        for x in bills:
            if x == 5:
                five_dollers += 1
            elif x == 10:
                if five_dollers > 0:
                    five_dollers -= 1
                else:
                    return False
                ten_dollers += 1
            else:
                if five_dollers > 0 and ten_dollers > 0:
                    five_dollers -= 1
                    ten_dollers -= 1
                elif five_dollers > 2 :
                    five_dollers -= 3
                else:
                    return False
            print(five_dollers, ten_dollers)
        return True