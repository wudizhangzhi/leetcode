class BstNode(object):
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def findMin(self):
        currentNode = self
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode

    def replace_node_in_parent(self, node=None):
        if self.parent is None:
            self.parent = node
        elif self.parent.left == self:
            self.parent.left = node
        elif self.parent.right == self:
            self.parent.right = node

        if node:
            node.parent = self.parent

    def delete(self, key):
        if self.key == key:
            if self.left and self.right:
                rightminum = self.right.findMin()
                self.key = rightminum.key
                rightminum.delete(rightminum.key)
            elif self.left:
                self.replace_node_in_parent(self.left)
            elif self.right:
                self.replace_node_in_parent(self.right)
            else:
                self.replace_node_in_parent(None)

        elif self.key < key and self.right:
            self.right.delete(key)
        elif self.key < key and self.left:
            self.left.delete(key)

    def insert(self, key):
        if self.key == key:
            return
        elif self.key > key:
            if self.left is None:
                self.left = BstNode(key, parent=self)
            else:
                self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key, parent=self)
            else:
                self.right.insert(key)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def test():
    import random

    b = BstNode(50)
    for _ in range(50):
        b.insert(random.randint(0, 100))
    b.display()


if __name__ == '__main__':
    # test()
    a = [5, 9, 20, 30, 1, 3, 6, 11, 15, 22, 26, 32]
    b = BstNode(10)
    for i in a:
        b.insert(i)
    b.display()
    b.delete(20)
    b.display()
