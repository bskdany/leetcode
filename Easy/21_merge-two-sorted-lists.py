from types import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:        
        if(list1==None):
            return list2
        elif(list2==None):
            return list1

        mainNode, comparasonNode = list1, list2
        if(list1.val>list2.val):
            mainNode, comparasonNode = list2, list1
        
        nodeToReturn = mainNode

        #mainNode is the list that starts with the smallest value
        #comparason Node is the list of nodes that are going to be tested against
        #the node values in the list determined by mainNode
        while(comparasonNode!=None):
            
            # valueToCompare will be inserted iff it is bigger than the value in mainValue
            if(mainNode.next==None):
                mainNode.next = comparasonNode
                return nodeToReturn

            if(comparasonNode.val<=mainNode.next.val):
                tempNode = comparasonNode.next
                comparasonNode.next = mainNode.next
                mainNode.next = comparasonNode
                comparasonNode = tempNode
            
            mainNode = mainNode.next

        return nodeToReturn

S1 = Solution
first = ListNode(1)
first.next = ListNode(2)
first.next.next = ListNode(5)
first.next.next.next = ListNode(8)

second = ListNode(1)
second.next = ListNode(2)
second.next.next = ListNode(5)
second.next.next.next = ListNode(8)

S1.mergeTwoLists(S1, first, second)
