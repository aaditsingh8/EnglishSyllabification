class Node(object):
    def __init__(self, data='', parent=None):
        self.data = data
        self.children = []
        self.parent = parent

    def add_child(self, data):
        new_node = Node(data, self)
        self.children.append(new_node)
        return new_node

    def __str__(self):
        curr = self
        res = ''
        while curr:
            res = curr.data + res
            curr = curr.parent
        return res


if __name__ == '__main__':
    root = Node()
    root.add_child('a')
    child = root.add_child('b')
    root.add_child('c')
    child.add_child('d')
    child.add_child('e')
    child2 = child.add_child('f')
    child3 = child2.add_child('g')

    print(child3)
