class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      if not list1:
        return list2
      elif not list2:
        return list1


      head = None
      if list1.val <= list2.val:
        head = list1
        list1 = list1.next
      else:
        head = list2
        list2 = list2.next

      current = head

      while list1 and list2:
        if list1.val <= list2.val:
          current.next = list1
          current = current.next
          list1 = list1.next
        else:
          current.next = list2
          current = current.next
          list2 = list2.next

      if list1:
        current.next = list1
      elif list2:
        current.next = list2
      return head

        