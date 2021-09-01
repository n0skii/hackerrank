# Node is defined as
# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.left: Node = None
#         self.right: Node = None


def check_bin(node, _min, _max):
    if not node:
        return True
    if node.data <= _min or node.data >= _max:
        return False
    return check_bin(node.left, _min, node.data) and check_bin(
        node.right, node.data, _max
    )


def check_binary_search_tree_(root):
    return check_bin(root, -1, float("inf"))
