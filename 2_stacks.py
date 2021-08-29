import sys


class Stack:
    def __init__(self) -> None:
        self._elems: list = list()

    def push(self, value):
        self._elems.append(value)

    def pop(self):
        value = self._elems[-1]
        self._elems.pop()
        return value

    def peek(self):
        return None if len(self._elems) == 0 else self._elems[-1]

    def isEmpty(self):
        return True if len(self._elems) == 0 else False

    def clear(self):
        self._elems = list()


def main(data: list):
    back = Stack()
    front = Stack()

    for d in data:
        if d[0] == "1":
            value = int(d[1])

            front.push(value)
        if d[0] == "2":
            if back.isEmpty():
                while not front.isEmpty():
                    back.push(front.pop())
            back.pop()

        if d[0] == "3":
            if back.isEmpty():
                while not front.isEmpty():
                    back.push(front.pop())
            print(back.peek())


if __name__ == "__main__":
    data = list()
    for line in sys.stdin.readlines()[1:]:
        data.append(line.replace("\n", "").split(" "))

    main(data)
