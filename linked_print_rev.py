def reversePrint(llist):
    if llist.next == None:
        print(llist.data)
        return

    holder = list()
    while 1:
        holder.append(str(llist.data))
        if not llist.next:
            break
        llist = llist.next

    print("\n".join(list(reversed(holder))))
