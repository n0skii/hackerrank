def has_cycle(head):
    visited = dict()
    if head.next == None:
        return 0

    while head.next != None:
        if head in visited:
            return 1
        else:
            visited[head] = True
            head = head.next

    return 0
