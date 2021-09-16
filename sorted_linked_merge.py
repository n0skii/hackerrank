def mergeLists(head1, head2):

    if head1 and head2:
        if head1.data <= head2.data:
            mergedListHead = head1
            head1 = head1.next
        else:
            mergedListHead = head2
            head2 = head2.next

    mergedListHead.next = None
    mergedList = mergedListHead

    while head1 or head2:
        if head1 == None:
            mergedList.next = head2
            mergedList = mergedList.next
            head2 = head2.next
            continue
        if head2 == None:
            mergedList.next = head1
            mergedList = mergedList.next
            head1 = head1.next
            continue
        if head1.data <= head2.data:
            mergedList.next = head1
            mergedList = mergedList.next
            head1 = head1.next
        else:
            mergedList.next = head2
            mergedList = mergedList.next
            head2 = head2.next
    return mergedListHead
