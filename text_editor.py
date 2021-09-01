import sys


class Stack(object):
    def __init__(self, data=None, action=None, next=None) -> None:
        super().__init__()
        self.next: Stack = next
        self.data = data
        self.action = action


def main(queries):
    overallArr = ""
    actions = Stack()

    for q in queries:
        if q[0] == "1":
            actions = Stack(data=len(q[1]), action="add", next=actions)
            overallArr += q[1]
        if q[0] == "2":
            toDelete = int(q[1])
            removed = overallArr[-toDelete:]
            actions = Stack(data=removed, action="del", next=actions)
            overallArr = overallArr[:-toDelete]
        if q[0] == "3":
            print(overallArr[int(q[1]) - 1])
        if q[0] == "4":
            if actions.action == "del":
                overallArr += actions.data
            else:
                overallArr = overallArr[: -actions.data]
            actions = actions.next


if __name__ == "__main__":
    data = [line.replace("\n", "").split(" ") for line in sys.stdin.readlines()[1:]]

    main(data)
