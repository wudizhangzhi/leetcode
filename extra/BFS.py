"""
广度优先算法
Breadth-first search(BFS) algorithm
"""
from queue import Queue

class Node:
    inst_count = 0

    def __init__(self):
        self.value = Node.inst_count
        self.left = None
        self.right = None
        Node.inst_count += 1

    def __str__(self):
        return '%s' % self.value

    def get_children(self):
        children = []
        if self.left:
            children.append(self.left)
        if self.right:
            children.append(self.right)
        return children


def construct_path(node, meta):
    all_path = [node]
    while node in meta:
        all_path.append(meta[node])
        node = meta[node]
    return all_path

def breadth_first_search(problem, target):
    fifo_queue = Queue()
    fifo_queue.put(problem)

    # open_set = []
    meta = {}
    closed_set = []
    while not fifo_queue.empty():
        subtree_root = fifo_queue.get()
        print('search: %s' % subtree_root)

        if subtree_root.value == target:
            return construct_path(subtree_root, meta)

        for child in subtree_root.get_children():
            if child in closed_set:
                continue
            fifo_queue.put(child)
            meta[child] = subtree_root

        closed_set.append(subtree_root)

def traverse(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(node) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level = next_level

def generate_problem():
    root = Node()
    to_add = [root]
    def add_node(node):
        node.left = Node()
        node.right = Node()
        to_add.extend([node.left, node.right])
    for i in range(20):
        add_node(to_add[i])
    return root

if __name__ == '__main__':
    problem = generate_problem()
    traverse(problem)
    all_path = breadth_first_search(problem, target=10)
    print([i.value for i in all_path])
