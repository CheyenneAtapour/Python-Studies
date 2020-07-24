def removeDuplicates(head):
    if head == None:
        return head
    current = head
    while not current == None:
        prev = current.data
        while not current.next == None and current.next.data == prev: # dup value ahead
            current.next = current.next.next
        current = current.next
    return head