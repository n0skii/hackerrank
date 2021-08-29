class Node(object):
    def __init__(self) -> None:
        super().__init__()
        self.childMap = dict()
        self.childNum = 0
        self.count = -1


def matchingStrings(strings, queries):
    trie = Node()

    for s in strings:
        curNode: Node = trie
        for char in s:
            if char in curNode.childMap:
                curNode = curNode.childMap[char]
            else:
                newNode = Node()
                newNode.count = 0
                curNode.childMap[char] = newNode
                curNode = newNode
        curNode.count += 1

    for q in queries:
        curNode: Node = trie
        alreadyPrinted = False
        for char in q:
            if char in curNode.childMap:
                curNode = curNode.childMap[char]
            else:
                print("0")
                alreadyPrinted = True
                break
        if not alreadyPrinted:
            print(curNode.count)


def main():
    # something = ["[][[])", "[()({})[]]"]
    something = [[["ab", "ab", "abc"], ["ab", "abc", "bc"]]]
    for s in something:
        matchingStrings(s[0], s[1])


if __name__ == "__main__":
    main()
