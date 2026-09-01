# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # First approach
        # check = set()
        # curr = head
        # while curr != None:
        #     if curr in check:
        #         return True
        #     check.add(curr)
        #     curr = curr.next
        # return False



        #Second approach --- floyd hare and tortoise algo

        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast == None or fast.next == None:
                return None
            slow = slow.next
            fast = fast.next.next
        return True
