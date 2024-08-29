# Find length of Loop
# Difficulty: Easy
# Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.

#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #Your code here
        count=0
        slowMove=head
        fastMove=head
        while fastMove and fastMove.next:
            fastMove=fastMove.next.next
            slowMove=slowMove.next
            if fastMove==None:
                break
            if fastMove==slowMove:
                count=1
                slowMove=slowMove.next
                while fastMove!=slowMove:
                    count+=1
                    slowMove=slowMove.next
                return count
        return 0
